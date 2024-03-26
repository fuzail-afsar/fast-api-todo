from fastapi import APIRouter

from app.core.db import DB
from app.models.todo import Todo, UpdateTodo
from app.crud import todo as todoCrud

router = APIRouter()


@router.post("/", response_model=Todo)
def create_todo(todo: Todo, db: DB):
    return todoCrud.create(todo, db)


@router.get("/", response_model=list[Todo])
def get_todos(db: DB):
    return todoCrud.fetch(db)


@router.patch("/{id}", response_model=Todo)
def update_todo(id: str, update_todo: UpdateTodo, db: DB):
    return todoCrud.update_by_id(int(id), update_todo.content, db)


@router.delete("/{id}")
def delete_todo(id: str, db: DB):
    todoCrud.delete_by_id(int(id), db)


@router.delete("/")
def delete_all_todos(db: DB):
    todoCrud.delete_all(db)
