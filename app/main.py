from fastapi import FastAPI
from app.core.config import settings
from app.core.exceptions.handlers import register_exception_handlers
from app.modules import models  # noqa: F401  (register all models)

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    version="1.0.0",
    description="Ecommerce API",
)

register_exception_handlers(app)
