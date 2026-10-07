from app.modules.authentication.schemas.authentication_response import (
    AuthenticationResponse,
)
from app.modules.authentication.schemas.token import TokenResponse
from app.modules.authentication.service import AuthenticatedUser
from app.modules.users.schemas.user_response import UserResponse


def to_authentication_response(
    authenticated: AuthenticatedUser,
) -> AuthenticationResponse:
    return AuthenticationResponse(
        user=UserResponse.model_validate(authenticated.user),
        token=TokenResponse(
            access_token=authenticated.access_token,
            token_type="bearer",
            expires_in=authenticated.expires_in,
        ),
    )
