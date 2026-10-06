from typing import Annotated

from pydantic import BaseModel, EmailStr, Field

from app.core.validators import Password, Username


class RegisterRequest(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=255)]
    username: Username
    email: Annotated[EmailStr, Field(min_length=1, max_length=255)]
    password: Password
    language: Annotated[str, Field(min_length=2, max_length=10)]
