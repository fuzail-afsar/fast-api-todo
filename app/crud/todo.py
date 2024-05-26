from sqlmodel import select, delete

from app.core.db import DB
from app.models.todo import CreateTodo, Todo, UpdateTodo


def create(todo: CreateTodo, db: DB):
    try:
        todo_created: Todo = Todo.model_validate(todo)
        db.add(todo_created)
        db.commit()
        db.refresh(todo_created)

        return todo_created
    except Exception as e:
        raise e


def fetch(db: DB):
    try:
        todos: list[Todo] = db.exec(select(Todo)).all()

        return todos
    except Exception as e:
        raise e


def get_by_id(id: int, db: DB):
    try:
        statement = select(Todo).where(Todo.id == id)
        result: Todo = db.exec(statement).one()

        return result
    except Exception as e:
        raise e


def update_by_id(id: int, data: UpdateTodo, db: DB):
    try:
        todo = get_by_id(id, db)

        if not todo:
            raise "Todo not found!"

        updated_data = data.model_dump(exclude_unset=True)
        todo.sqlmodel_update(updated_data)

        db.add(todo)
        db.commit()
        db.refresh(todo)

        return todo
    except Exception as e:
        raise e


def delete_by_id(id: int, db: DB):
    try:
        todo = get_by_id(id, db)

        if not todo:
            raise "Todo not found!"

        db.delete(todo)
        db.commit()

        return True
    except Exception as e:
        raise e


def delete_all(db: DB):
    try:
        db.exec(delete(Todo))
        db.commit()

        return True
    except Exception as e:
        raise e
