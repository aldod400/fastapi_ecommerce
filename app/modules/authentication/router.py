from fastapi import APIRouter, Depends

from app.core.response import ApiResponse
from app.modules.authentication.dependencies import get_authentication_service
from app.modules.authentication.schemas.authentication_response import (
    AuthenticationResponse,
)
from app.modules.authentication.mappers import to_authentication_response
from app.modules.authentication.schemas.register import RegisterRequest
from app.modules.authentication.service import AuthenticationService
from app.core.i18n.translator import t
from app.modules.users.schemas.user_response import UserResponse

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", status_code=201)
async def register_user(
    register_request: RegisterRequest,
    authentication_service: AuthenticationService = Depends(get_authentication_service),
) -> ApiResponse[AuthenticationResponse]:
    """Register a new user."""
    authenticated = await authentication_service.register(register_request)

    return ApiResponse(
        status_code=201,
        message=t("auth.registration_successful"),
        data=to_authentication_response(authenticated),
    )


@router.get("/me", response_model=ApiResponse[UserResponse])
async def get_current_user(
    current_user: UserResponse = Depends(get_authentication_service),
) -> ApiResponse[UserResponse]:
    """Get the currently authenticated user."""
    return ApiResponse(
        status_code=200,
        message=t("auth.current_user_retrieved"),
        data=current_user,
    )