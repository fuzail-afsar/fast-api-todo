from sqlmodel import Field, SQLModel
from pydantic import EmailStr, SecretStr
from datetime import datetime


class BaseUser(SQLModel):
    email: str = Field(unique=True, index=True)
    name: str


class User(BaseUser, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str
    is_active: bool = True
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())


class CreateUser(BaseUser):
    password: SecretStr
    email: EmailStr


class CreatedUser(BaseUser):
    id: int
    created_at: datetime
    updated_at: datetime


class CurrentUser(CreatedUser):
    pass


class UpdateUser(SQLModel):
    name: str


class UpdatedUser(CreatedUser):
    pass
