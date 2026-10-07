import uuid
from collections.abc import Callable

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.modules.users.repository import UserRepository

type UserRepositoryFactory = Callable[[AsyncSession], UserRepository]


class UserLanguageLookup:
    """Looks up the language saved for a user, outside of a request's db session."""

    def __init__(
        self,
        session_factory: async_sessionmaker[AsyncSession],
        repository_factory: UserRepositoryFactory,
    ):
        self.session_factory = session_factory
        self.repository_factory = repository_factory

    async def __call__(self, user_id: str) -> str | None:
        """Return the language saved for the user, or None if there is no such user."""
        try:
            parsed_id = uuid.UUID(user_id)
        except ValueError:
            return None

        async with self.session_factory() as db:
            return await self.repository_factory(db).get_user_language(parsed_id)
