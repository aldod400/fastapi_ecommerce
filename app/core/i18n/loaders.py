import json
from pathlib import Path
from typing import Any, Protocol, cast

type Catalog = dict[str, str]


class MessageLoader(Protocol):
    def load(self) -> dict[str, Catalog]:
        """Return the messages of every locale as {locale: {key: text}}."""
        ...


class JsonMessageLoader:
    """Loads `<directory>/<locale>/<file>.json`; keys are prefixed with the file name."""

    def __init__(self, directory: Path):
        self.directory = directory

    def load(self) -> dict[str, Catalog]:
        return {
            locale_dir.name: self._load_locale(locale_dir)
            for locale_dir in sorted(self.directory.iterdir())
            if locale_dir.is_dir()
        }

    def _load_locale(self, locale_dir: Path) -> Catalog:
        catalog: Catalog = {}
        for file in sorted(locale_dir.glob("*.json")):
            content = json.loads(file.read_text(encoding="utf-8"))
            catalog.update(self._flatten(content, prefix=file.stem))
        return catalog

    def _flatten(self, content: dict[str, Any], prefix: str) -> Catalog:
        catalog: Catalog = {}
        for key, value in content.items():
            full_key = f"{prefix}.{key}"
            if isinstance(value, dict):
                catalog.update(
                    self._flatten(cast(dict[str, Any], value), prefix=full_key)
                )
            else:
                catalog[full_key] = str(value)
        return catalog
