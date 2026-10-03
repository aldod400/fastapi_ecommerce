from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic_core import ValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.core.config import settings


def error_response(status_code: int, message: str) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={"status_code": status_code, "message": message},
    )


def register_exception_handlers(app: FastAPI) -> None:

    @app.exception_handler(StarletteHTTPException)
    async def _(request: Request, exc: StarletteHTTPException) -> JSONResponse:
        return error_response(exc.status_code, str(exc.detail))

    @app.exception_handler(RequestValidationError)
    async def _(request: Request, exc: RequestValidationError) -> JSONResponse:
        error = exc.errors()[0]
        field = ".".join(str(part) for part in error["loc"][1:])
        return error_response(422, f"{field}: {error['msg']}")

    @app.exception_handler(ValidationError)
    async def _(request: Request, exc: ValidationError) -> JSONResponse:
        return error_response(422, str(exc))

    @app.exception_handler(Exception)
    async def _(request: Request, exc: Exception) -> JSONResponse:
        if settings.debug:
            return error_response(500, exc.__class__.__name__ + ": " + str(exc))
        return error_response(500, "Internal server error")
