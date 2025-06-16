from fastapi import FastAPI
from crud import crud_router
from Internship.FastAPI.auth import auth_router
from Internship.FastAPI.logsign import user_router

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Welcome to FastAPI Project"}

app.include_router(crud_router, prefix="/crud", tags=["CRUD Operations"])
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(user_router, prefix="/user", tags=["User Login/Signup"])
