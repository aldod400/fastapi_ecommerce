from datetime import UTC, datetime, timedelta
from typing import Any

import jwt
import uuid

from pwdlib import PasswordHash

from app.core.config import settings

password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)


def create_access_token(
    subject: uuid.UUID, expires_delta: timedelta | None = None
) -> str:
    now = datetime.now(UTC)
    expires_at = now + (
        expires_delta or timedelta(minutes=settings.access_token_expire_minutes)
    )
    payload: dict[str, Any] = {"sub": str(subject), "iat": now, "exp": expires_at}
    return jwt.encode(payload, settings.app_key, algorithm=settings.jwt_algorithm)


def decode_access_token(token: str) -> dict[str, Any] | None:
    """Return the token payload, or None if the token is invalid or expired."""
    try:
        return jwt.decode(
            token,
            settings.app_key,
            algorithms=[settings.jwt_algorithm],
            options={"require": ["sub", "exp"]},
        )
    except jwt.InvalidTokenError:
        return None
