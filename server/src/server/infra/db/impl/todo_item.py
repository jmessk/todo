from sqlalchemy.ext.asyncio import AsyncSession

from server.domain.model.todo_item import TodoItem
from server.domain.repository.todo_item import TodoItemRepository
from ..models.todo_item import TodoItem as DbTodoItem


class TodoItemRepositoryImpl(TodoItemRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, todo: TodoItem) -> TodoItem:
        # db_todo = DbTodoItem(**todo.dict())
        # self.session.add(db_todo)
        # await self.session.commit()
        # await self.session.refresh(db_todo)

        # return db_todo

        db_todo = DbTodoItem(
            id=todo.id,
            title=todo.title,
            description=todo.description,
            status=todo.status,
            created_at=todo.created_at,
            updated_at=todo.updated_at,
            deleted_at=todo.deleted_at,
        )

        self.session.add(db_todo)
        await self.session.commit()
        await self.session.refresh(db_todo)
        return todo

    async def find_all(self) -> list[TodoItem]:
        result = await self.session.execute(select(DbTodoItem))
        return [TodoItem.from_orm(todo) for todo in result.scalars().all()]

    async def find_by_id(self, todo_id: UUID) -> TodoItem | None:
        result = await self.session.execute(
            select(DbTodoItem).where(DbTodoItem.id == todo_id)
        )
        return TodoItem.from_orm(result.scalar()) if result else None

    async def find_by_status(self, completed: bool) -> TodoItem | None:
        result = await self.session.execute(
            select(DbTodoItem).where(DbTodoItem.completed == completed)
        )
        return TodoItem.from_orm(result.scalar()) if result else None

    async def delete(self, todo_id: UUID) -> bool:
        result = await self.session.execute(
            select(DbTodoItem).where(DbTodoItem.id == todo_id)
        )
        todo = result.scalar()
        if todo:
            await self.session.delete(todo)
            await self.session.commit()
            return True
        return False

    async def exists(self, todo_id: UUID) -> bool:
        result = await self.session.execute(
            select(DbTodoItem).where(DbTodoItem.id == todo_id)
        )
        return result.scalar() is not None
