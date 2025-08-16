from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


from .todo import Todo  # noqa: E402, F401
