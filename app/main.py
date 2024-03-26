from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.core.db import init_db, DB
from app.models.todo import Todo
from app.crud import todo as todoCrud
from app.api.main import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables...")
    init_db()
    yield


app = FastAPI(
    lifespan=lifespan,
    title="Todo API",
    version="0.0.1",
    servers=[{"url": "http://localhost:8000", "description": "Development Server"}],
)


app.include_router(api_router, prefix="/api")
