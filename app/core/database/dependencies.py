from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database.connection import SessionLocal


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
