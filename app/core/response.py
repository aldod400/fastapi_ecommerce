from math import ceil
from typing import Any

from pydantic import BaseModel, SerializerFunctionWrapHandler, model_serializer


class PaginationMeta(BaseModel):
    total: int
    page: int
    per_page: int
    total_pages: int
    next_page: int | None = None
    previous_page: int | None = None

    @classmethod
    def build(cls, total: int, page: int, per_page: int) -> "PaginationMeta":
        total_pages = ceil(total / per_page) if per_page > 0 else 0
        return cls(
            total=total,
            page=page,
            per_page=per_page,
            total_pages=total_pages,
            next_page=page + 1 if page < total_pages else None,
            previous_page=page - 1 if page > 1 else None,
        )


class ApiResponse[T](BaseModel):
    status_code: int
    message: str = "Success"
    data: T | None = None
    meta: PaginationMeta | None = None

    @model_serializer(mode="wrap")
    def _omit_empty_meta(self, handler: SerializerFunctionWrapHandler):
        serialized: dict[str, Any] = handler(self)
        if self.meta is None:
            serialized.pop("meta", None)
        return serialized
