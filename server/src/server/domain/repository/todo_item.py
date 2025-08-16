from abc import ABC, abstractmethod
from uuid_utils import UUID

from ..model.todo_item import TodoItem


class TodoItemRepository(ABC):
    @abstractmethod
    async def add(self, todo: TodoItem) -> TodoItem:
        pass

    @abstractmethod
    async def find_all(self) -> list[TodoItem]:
        pass

    @abstractmethod
    async def find_by_id(self, todo_id: UUID) -> TodoItem | None:
        pass

    @abstractmethod
    async def find_by_status(self, completed: bool) -> TodoItem | None:
        pass

    @abstractmethod
    async def delete(self, todo_id: UUID) -> bool:
        pass

    @abstractmethod
    async def exists(self, todo_id: UUID) -> bool:
        pass
