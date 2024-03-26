from sqlmodel import select, delete

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


def get_by_id(id: int, db: DB):
    statement = select(Todo).where(Todo.id == id)
    return db.exec(statement).one()


def update_by_id(id: int, content, db: DB):
    todo = get_by_id(id, db)
    todo.content = content

    db.add(todo)
    db.commit()
    db.refresh(todo)

    return todo


def delete_by_id(id: int, db: DB):
    todo = get_by_id(id, db)

    db.delete(todo)
    db.commit()


def delete_all(db: DB):
    db.exec(delete(Todo))
    db.commit()
