from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, select

from app.core.db import DB
from app.models.todo import Todo


def create(todo: Todo, db: DB):
    print("todo", todo)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def fetch(db: DB):
    todos = db.exec(select(Todo)).all()
    return todos
