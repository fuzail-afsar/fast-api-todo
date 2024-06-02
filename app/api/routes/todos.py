from app.api.deps import Pagination
from fastapi import APIRouter, status, HTTPException

from app.core.db import DB
from app.models.todo import CreateTodo, UpdateTodo, Todo
from app.crud import todo as todoCrud

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_todo(todo: CreateTodo, db: DB) -> Todo:
    todo_created = todoCrud.create(todo, db)

    if not todo_created:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Invalid request data",
        )

    return todo_created


@router.get("/")
def get_todos(db: DB, pagination: Pagination) -> list[Todo]:
    return todoCrud.fetch(db, **pagination)


@router.get("/{id}")
def get_todo(id: int, db: DB) -> Todo:
    todo = todoCrud.get_by_id(id, db)

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found"
        )

    return todo


@router.patch("/{id}")
def update_todo(id: str, update_todo: UpdateTodo, db: DB) -> Todo:
    todo = todoCrud.update_by_id(int(id), update_todo, db)

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found"
        )

    return todo


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(id: str, db: DB):
    todo = todoCrud.delete_by_id(int(id), db)

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found"
        )

    return


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_all_todos(db: DB):
    todoCrud.delete_all(db)

    return
