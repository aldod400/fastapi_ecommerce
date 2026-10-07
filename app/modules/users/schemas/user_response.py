from datetime import datetime
import uuid

from pydantic import BaseModel, ConfigDict


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    username: str
    email: str
    is_active: bool
    language: str
    created_at: datetime
    updated_at: datetime
