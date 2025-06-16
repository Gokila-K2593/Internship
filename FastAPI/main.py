from fastapi import FastAPI
from crud import crud_router
from auth import auth_router
from user import user_router
from sqlmodel import SQLModel
from crud import engine  # Import engine to create tables

app = FastAPI()

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(crud_router,prefix="/crud")
app.include_router(auth_router,prefix="/auth")
app.include_router(user_router,prefix="/user")
