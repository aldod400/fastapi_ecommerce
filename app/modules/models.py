# Import every module's models here so they register on Base.metadata for Alembic.
from app.modules.users.model import User

__all__ = ["User"]
