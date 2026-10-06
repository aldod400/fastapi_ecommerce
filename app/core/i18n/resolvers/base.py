from typing import Protocol

from fastapi import Request


class LocaleResolver(Protocol):
    async def resolve(self, request: Request) -> list[str]:
        """Return the languages this source suggests for the request, most preferred first."""
        ...
