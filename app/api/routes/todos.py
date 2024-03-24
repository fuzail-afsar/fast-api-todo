from fastapi import APIRouter

from app.core.db import DB
from app.models.todo import Todo
from app.crud import todo as todoCrud

router = APIRouter()


@router.post("/todos/", response_model=Todo)
def create_todo(todo: Todo, db: DB):
    return todoCrud.create(todo, db)


@router.get("/todos/", response_model=list[Todo])
def get_todos(db: DB):
    return todoCrud.fetch(db)
