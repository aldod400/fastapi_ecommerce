import uuid

from app.core.database.connection import SessionLocal
from app.modules.users.repository import UserRepository


async def get_user_language(user_id: str) -> str | None:
    """Return the language saved for the user, or None if there is no such user."""
    try:
        parsed_id = uuid.UUID(user_id)
    except ValueError:
        return None

    async with SessionLocal() as db:
        return await UserRepository(db).get_user_language(parsed_id)
