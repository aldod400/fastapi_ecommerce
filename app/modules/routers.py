from fastapi import APIRouter, FastAPI

from app.modules.authentication import router as authentication_router

router = APIRouter(prefix="/api")

router.include_router(authentication_router.router)


def register_routers(app: FastAPI) -> None:
    app.include_router(router)
