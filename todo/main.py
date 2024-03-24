# main.py
from contextlib import asynccontextmanager
from typing import Union, Optional, Annotated
from todo import settings
from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi import FastAPI, Depends

class Todo(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    content: str = Field(index = True)
    
connection_string = str(settings.DATABASE_URL).replace('postgresql', 'postgresql+psycopg')

engine = create_engine(connection_string, connect_args = {'sslmode': 'require'}, pool_recycle = 300)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    
@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Creating tables...')
    create_db_and_tables()
    yield

app = FastAPI(
        lifespan = lifespan, 
        title = 'Todo API', 
        version = '0.0.1', 
        servers = [
            {
                'url': 'http://localhost:8000',
                'description': 'Development Server'
            }
        ]
    )

def get_session():
    with Session(engine) as session:
        yield session
        
@app.get('/')
def read_root():
    return {'hello': 'world'}

@app.post('/todos/', response_model = Todo)
def create_todo(todo: Todo, session: Annotated[Session, Depends(get_session)]):
    print('todo', todo);
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

@app.get('/todos/', response_model = list[Todo])
def read_todos(session: Annotated[Session, Depends(get_session)]):
    todos = session.exec(select(Todo)).all()
    return todos