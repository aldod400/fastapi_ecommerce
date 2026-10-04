from typing import Annotated

from pydantic import AfterValidator, Field
from pydantic_core import PydanticCustomError


def validate_username(value: str) -> str:
    if not (value.isascii() and value.isalnum()):
        raise PydanticCustomError(
            "invalid_username",
            "Username may only contain letters and digits, with no spaces or special characters",
        )
    return value


Username = Annotated[str, Field(max_length=255), AfterValidator(validate_username)]
