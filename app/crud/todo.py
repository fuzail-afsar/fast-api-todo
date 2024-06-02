from sqlmodel import select, delete

from app.core.db import DB
from app.models.todo import CreateTodo, Todo, UpdateTodo


def create(todo: CreateTodo, db: DB) -> Todo:
    try:
        todo_created: Todo = Todo.model_validate(todo)
        db.add(todo_created)
        db.commit()
        db.refresh(todo_created)

        return todo_created
    except Exception as e:
        print("Exception:", e)
        return None


def fetch(db: DB, offset, limit):
    try:
        todos: list[Todo] = db.exec(select(Todo).offset(offset).limit(limit)).all()

        return todos
    except Exception as e:
        print("Exception:", e)
        return None


def get_by_id(id: int, db: DB):
    try:
        todo: Todo = db.get(Todo, id)

        return todo
    except Exception as e:
        print("Exception:", e)
        return None


def update_by_id(id: int, data: UpdateTodo, db: DB):
    try:
        todo = get_by_id(id, db)

        if not todo:
            return None

        updated_data = data.model_dump(exclude_unset=True)
        todo.sqlmodel_update(updated_data)

        db.add(todo)
        db.commit()
        db.refresh(todo)

        return todo
    except Exception as e:
        print("Exception:", e)
        return None


def delete_by_id(id: int, db: DB):
    try:
        todo = get_by_id(id, db)

        if not todo:
            None

        db.delete(todo)
        db.commit()

        return True
    except Exception as e:
        print("Exception:", e)
        return None


def delete_all(db: DB):
    try:
        db.exec(delete(Todo))
        db.commit()

        return True
    except Exception as e:
        print("Exception:", e)
        return None
