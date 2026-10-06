from pathlib import Path

from app.core.config import settings
from app.core.i18n.loaders import Catalog, JsonMessageLoader, MessageLoader
from app.core.i18n.locale import get_locale


class Translator:
    def __init__(self, loader: MessageLoader, default_locale: str):
        self.default_locale = default_locale
        self._catalogs: dict[str, Catalog] = loader.load()

    @property
    def supported_locales(self) -> list[str]:
        return list(self._catalogs)

    def translate(self, key: str, locale: str | None = None, **params: object) -> str:
        """Translate `key` for `locale`, the current request locale, or the default one.

        Falls back to the default locale, then to the key itself.
        """
        locale = locale or get_locale() or self.default_locale
        text = self._catalogs.get(locale, {}).get(key)
        if text is None:
            text = self._catalogs.get(self.default_locale, {}).get(key, key)
        return text.format(**params) if params else text


translator = Translator(
    loader=JsonMessageLoader(Path(__file__).parent / "locales"),
    default_locale=settings.default_locale,
)

t = translator.translate
