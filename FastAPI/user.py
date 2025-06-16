from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Field, Session, create_engine, select
from pydantic import BaseModel
from passlib.hash import bcrypt
from jose import jwt
from fastapi import APIRouter
user_router=APIRouter()
DATABASE_URL = "postgresql://gokila:goki@localhost:5432/fastapi_db"
engine = create_engine(DATABASE_URL, echo=True)
SECRET_KEY = "secret"
ALGORITHM = "HS256"
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str 
class UserInput(BaseModel):
    username: str
    password: str
@user_router.post("/signup")
def signup(user: UserInput):
    with Session(engine) as session:
        existing = session.exec(select(User).where(User.username == user.username)).first()
        if existing:
            raise HTTPException(status_code=400, detail="User exists")
        hashed = bcrypt.hash(user.password)
        new_user = User(username=user.username, password=hashed)
        session.add(new_user)
        session.commit()
        return {"msg": "Signup success"}
@user_router.post("/login")
def login(user: UserInput):
    with Session(engine) as session:
        db_user = session.exec(select(User).where(User.username == user.username)).first()
        if not db_user or not bcrypt.verify(user.password, db_user.password):
            raise HTTPException(status_code=401, detail="Invalid login")
        token = jwt.encode({"sub": db_user.username}, SECRET_KEY, algorithm=ALGORITHM)
        return {"token": token}
