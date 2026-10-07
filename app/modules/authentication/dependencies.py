from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database.dependencies import get_db
from app.modules.authentication.service import AuthenticationService
from app.modules.users.repository import UserRepository


async def get_authentication_service(
    db: AsyncSession = Depends(get_db),
) -> AuthenticationService:
    user_repository = UserRepository(db)
    return AuthenticationService(db, user_repository)
