from pydantic import BaseModel, Field
from datetime import datetime
from uuid_utils import UUID, uuid7


class TodoItem(BaseModel):
    id: UUID = Field(default_factory=uuid7)
    title: str = Field(max_length=200)
    description: str | None = Field(default=None, max_length=500)
    status: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime | None = Field(default=None)
    deleted_at: datetime | None = Field(default=None)

    @classmethod
    def create(cls, title: str, description: str | None = None) -> "TodoItem":
        return cls(
            title=title,
            description=description,
        )

    def update(self, title: str | None = None, description: str | None = None):
        if title is not None:
            self.title = title

        if description is not None:
            self.description = description
