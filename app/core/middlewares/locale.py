from collections.abc import Sequence

from fastapi import FastAPI, Request, Response
from starlette.middleware.base import RequestResponseEndpoint

from app.core.i18n import set_locale
from app.core.i18n.resolvers import LocaleResolver


def register_locale_middleware(
    app: FastAPI,
    resolvers: Sequence[LocaleResolver],
    supported_locales: Sequence[str],
    default_locale: str,
) -> None:
    async def resolve_locale(request: Request) -> str:
        """Return the first supported language suggested by the resolvers, in order."""
        for resolver in resolvers:
            for language in await resolver.resolve(request):
                if language in supported_locales:
                    return language
        return default_locale

    @app.middleware("http")
    async def _(request: Request, call_next: RequestResponseEndpoint) -> Response:
        set_locale(await resolve_locale(request))
        return await call_next(request)
