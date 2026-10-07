from pydantic import BaseModel

from app.modules.authentication.schemas.token import TokenResponse
from app.modules.users.schemas.user_response import UserResponse


class AuthenticationResponse(BaseModel):
    user: UserResponse
    token: TokenResponse
