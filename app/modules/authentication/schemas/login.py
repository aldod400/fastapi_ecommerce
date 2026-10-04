from typing_extensions import Annotated

from pydantic import BaseModel, EmailStr, Field

from app.core.validators.password import Password


class LoginRequest(BaseModel):
    email: Annotated[EmailStr, Field(min_length=1, max_length=255)]
    password: Password
