from __future__ import annotations

"""SQLAlchemy Declarative Base と Alembic autogenerate 用 metadata 集約ポイント。

新しいモデルを追加したら、このファイルで import し、Base.metadata にテーブルを集約させる。
"""
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

from app.db.models.todo import Todo
