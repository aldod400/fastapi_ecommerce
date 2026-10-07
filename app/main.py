from fastapi import FastAPI
from app.core.config import settings
from app.core.exceptions.handlers import register_exception_handlers
from app.core.middlewares import register_middlewares
from app.modules.routers import register_routers

from app.modules import models  # noqa: F401  (register all models)

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    version="1.0.0",
    description="Ecommerce API",
)

register_middlewares(app)

register_exception_handlers(app)

register_routers(app)
