from app.api.deps import Pagination
from fastapi import APIRouter, status, HTTPException

from app.core.db import DB
from app.models.user import CreatedUser, CreateUser
from app.crud import user as userCrud

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: CreateUser, db: DB) -> CreatedUser:
    user_db = userCrud.get_user_by_email(user.email, db)

    if user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists"
        )

    return userCrud.create(user, db)
