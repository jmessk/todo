from pydantic import BaseModel
from uuid import uuid4

class TodoItem(BaseModel):
    id: int
    title: str
    description: str | None = None
    status: bool = False
    created_at: str
    updated_at: str | None = None
