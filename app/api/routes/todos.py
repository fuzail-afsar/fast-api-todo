from app.api.deps import Pagination
from fastapi import APIRouter, status, HTTPException

from app.core.db import DB
from app.models.todo import CreateTodo, UpdateTodo, Todo
from app.crud import todo as todoCrud

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_todo(todo: CreateTodo, db: DB) -> Todo:
    try:
        return todoCrud.create(todo, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail={"error": str(e)}
        )


@router.get("/")
def get_todos(db: DB, pagination: Pagination) -> list[Todo]:
    try:
        return todoCrud.fetch(db, **pagination)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail={"error": str(e)}
        )


@router.get("/{id}")
def get_todo(id: int, db: DB) -> Todo:
    try:
        result = todoCrud.get_by_id(id, db)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail={"error": str(e)}
        )


@router.patch("/{id}")
def update_todo(id: str, update_todo: UpdateTodo, db: DB) -> Todo:
    try:
        return todoCrud.update_by_id(int(id), update_todo, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail={"error": str(e)}
        )


@router.delete("/{id}")
def delete_todo(id: str, db: DB):
    try:
        todoCrud.delete_by_id(int(id), db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail={"error": str(e)}
        )


@router.delete("/")
def delete_all_todos(db: DB):
    try:
        todoCrud.delete_all(db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail={"error": str(e)}
        )
