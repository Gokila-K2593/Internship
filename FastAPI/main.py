# Import FastAPI to create the web application
from fastapi import FastAPI

# Import routers from different modules
from crud import crud_router
from auth import auth_router
from user import user_router
from rbac import rbac_router
from booking import booking_router


from sqlmodel import SQLModel
from database import engine


# Create FastAPI app instance
app = FastAPI()

# This function runs when the server starts

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)    # It will create tables in the database if they don’t exist

# Include the CRUD routes and set prefix as /crud
app.include_router(crud_router, prefix="/crud")
app.include_router(auth_router, prefix="/auth")
app.include_router(user_router, prefix="/user")
app.include_router(rbac_router, prefix="/rbac")
app.include_router(booking_router,prefix="/booking")


