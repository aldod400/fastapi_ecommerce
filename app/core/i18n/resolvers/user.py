from collections.abc import Awaitable, Callable

from fastapi import Request

from app.core.security import decode_access_token

type UserLanguageProvider = Callable[[str], Awaitable[str | None]]


class UserLocaleResolver:
    """Suggests the language saved for the user who owns the bearer token."""

    def __init__(self, get_user_language: UserLanguageProvider):
        self.get_user_language = get_user_language

    async def resolve(self, request: Request) -> list[str]:
        user_id = self._user_id(request)
        if user_id is None:
            return []

        language = await self.get_user_language(user_id)
        return [language] if language else []

    def _user_id(self, request: Request) -> str | None:
        scheme, _, token = request.headers.get("authorization", "").partition(" ")
        if scheme.lower() != "bearer":
            return None

        payload = decode_access_token(token.strip())
        return str(payload["sub"]) if payload else None
