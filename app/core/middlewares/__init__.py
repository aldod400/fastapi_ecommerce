from fastapi import FastAPI

from app.core.i18n import translator
from app.core.i18n.resolvers import HeaderLocaleResolver, UserLocaleResolver
from app.core.middlewares.locale import register_locale_middleware
from app.modules.users.locale import get_user_language


def register_middlewares(app: FastAPI) -> None:
    register_locale_middleware(
        app,
        # Checked in order; the first supported language wins.
        resolvers=[UserLocaleResolver(get_user_language), HeaderLocaleResolver()],
        supported_locales=translator.supported_locales,
        default_locale=translator.default_locale,
    )
