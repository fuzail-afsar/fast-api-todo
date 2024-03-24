from sqlmodel import SQLModel, Field
from typing import Optional


class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(index=True)


class UpdateTodo(SQLModel):
    content: str
