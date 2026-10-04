from typing import Annotated

from pydantic import AfterValidator, Field
from pydantic_core import PydanticCustomError

PASSWORD_SYMBOLS = set("@$!%*#?&")


def validate_password(value: str) -> str:
    if not (
        any(character.isascii() and character.isalpha() for character in value)
        and any(character.isascii() and character.isdigit() for character in value)
        and all(
            character.isascii() and (character.isalnum() or character in PASSWORD_SYMBOLS)
            for character in value
        )
    ):
        raise PydanticCustomError(
            "invalid_password",
            "Password must contain at least one letter and one digit, "
            "and may only contain letters, digits, or @$!%*#?&",
        )
    return value


Password = Annotated[str, Field(min_length=8, max_length=255), AfterValidator(validate_password)]
