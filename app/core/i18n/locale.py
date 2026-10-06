from contextvars import ContextVar

_current_locale: ContextVar[str | None] = ContextVar("current_locale", default=None)


def set_locale(locale: str) -> None:
    _current_locale.set(locale)


def get_locale() -> str | None:
    return _current_locale.get()
