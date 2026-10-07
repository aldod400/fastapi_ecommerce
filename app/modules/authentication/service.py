from dataclasses import dataclass

from app.core.config import settings
from app.core.security import create_access_token, hash_password
from app.modules.authentication.schemas.register import RegisterRequest
from app.modules.users.model import User
from app.modules.users.repository import UserRepository
from app.core.exceptions.errors import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.i18n.translator import t


@dataclass(frozen=True)
class AuthenticatedUser:
    user: User
    access_token: str
    expires_in: int


class AuthenticationService:
    def __init__(self, db: AsyncSession, user_repo: UserRepository):
        self.db = db
        self.user_repo = user_repo

    async def register(self, register_request: RegisterRequest) -> AuthenticatedUser:
        username_exists = await self.user_repo.get_user_by_username(
            register_request.username
        )

        if username_exists:
            raise ValidationError(t("auth.username_already_exists"))

        email_exists = await self.user_repo.get_user_by_email(register_request.email)
        if email_exists:
            raise ValidationError(t("auth.email_already_exists"))

        user: User = await self.user_repo.create_user(
            User(
                name=register_request.name,
                username=register_request.username,
                email=register_request.email,
                password=hash_password(register_request.password),
                is_active=True,
                language=register_request.language,
            )
        )

        await self.db.commit()

        await self.db.refresh(user)

        return self._authenticate(user)

    def _authenticate(self, user: User) -> AuthenticatedUser:
        return AuthenticatedUser(
            user=user,
            access_token=create_access_token(user.id),
            expires_in=settings.access_token_expire_minutes * 60,
        )
