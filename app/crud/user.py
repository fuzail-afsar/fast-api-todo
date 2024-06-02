from pydantic import EmailStr
from sqlmodel import select

from app.core.db import DB
from app.models.user import CreateUser, CreatedUser, User
from app.utils.hash import get_password_hash


def create(user: CreateUser, db: DB) -> CreatedUser:
    try:
        user_created: User = User.model_validate(
            user,
            update={
                "hashed_password": get_password_hash(user.password.get_secret_value())
            },
        )

        db.add(user_created)
        db.commit()
        db.refresh(user_created)

        return user_created
    except Exception as e:
        return None


def get_user_by_email(email: EmailStr, db: DB):
    try:
        statement = select(User).where(User.email == email)
        user: User = db.exec(statement).first()
        if user:
            return user
        return None
    except Exception as e:
        return None
