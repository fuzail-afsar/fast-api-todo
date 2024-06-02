from sqlmodel import SQLModel, Field
from typing import Optional


class BaseTodo(SQLModel):
    content: str = Field(index=True)


class Todo(BaseTodo, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class CreateTodo(BaseTodo):
    pass


class UpdateTodo(BaseTodo):
    pass
