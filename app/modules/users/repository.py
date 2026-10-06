import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.users.model import User
from sqlalchemy import select


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_user_by_email(self, email: str) -> User | None:
        return (
            await self.db.execute(select(User).where(User.email == email))
        ).scalar_one_or_none()

    async def get_user_by_username(self, username: str) -> User | None:
        return (
            await self.db.execute(select(User).where(User.username == username))
        ).scalar_one_or_none()

    async def get_user_language(self, user_id: uuid.UUID) -> str | None:
        return (
            await self.db.execute(select(User.language).where(User.id == user_id))
        ).scalar_one_or_none()

    async def create_user(self, user: User):
        self.db.add(user)
        await self.db.flush()

        return user
