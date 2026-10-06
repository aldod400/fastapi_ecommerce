from fastapi import Request


class HeaderLocaleResolver:
    """Suggests the languages of the Accept-Language header."""

    async def resolve(self, request: Request) -> list[str]:
        return parse_accept_language(request.headers.get("accept-language", ""))


def parse_accept_language(header: str) -> list[str]:
    """Return the header's languages by preference, e.g. "ar-EG,en;q=0.8" -> ["ar", "en"]."""
    weighted: list[tuple[float, str]] = []
    for part in header.split(","):
        tag, _, quality = part.strip().partition(";q=")
        weight = _parse_quality(quality)
        if weight > 0:
            weighted.append((weight, tag.split("-")[0].strip().lower()))

    weighted.sort(key=lambda item: item[0], reverse=True)
    return [language for _, language in weighted]


def _parse_quality(quality: str) -> float:
    if not quality:
        return 1.0
    try:
        return float(quality)
    except ValueError:
        return 0.0
