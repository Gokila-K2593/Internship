from fastapi import HTTPException,APIRouter
from sqlmodel import SQLModel, Field, Session, create_engine, select
from pydantic import BaseModel
from passlib.hash import bcrypt
from jose import jwt
from database import engine

user_router = APIRouter()    # Create API router

# JWT configuration values
SECRET_KEY = "secret"
ALGORITHM = "HS256"

# Define user table structure
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)  # Auto-generated primary key
    username: str                                          
    password: str                                           

class UserInput(BaseModel):    # Input model for signup and login
    username: str
    password: str


@user_router.post("/signup")     # Create a new user account
def signup(user: UserInput):
    with Session(engine) as session:    # Check if username already exists in the database
                                
        existing = session.exec(
            select(User).where(User.username == user.username)).first()

        if existing:     # If user already exists, return 400 error
            raise HTTPException(status_code=400, detail="User exists")

        hashed = bcrypt.hash(user.password)     # Hash the password before saving it

        new_user = User(username=user.username, password=hashed)     # Create a new User object
        session.add(new_user)
        session.commit()

        return {"msg": "Signup success"}


@user_router.post("/login")     # Validate user login and return JWT token
def login(user: UserInput):
    with Session(engine) as session:    # Find user in DB based on username
    
        db_user = session.exec(select(User).where(User.username == user.username)).first()
        
        if not db_user or not bcrypt.verify(user.password, db_user.password):    # If user not found or password doesn't match, return error
            raise HTTPException(status_code=401, detail="Invalid login")

        token = jwt.encode({"sub": db_user.username}, SECRET_KEY, algorithm=ALGORITHM)   # Create JWT token with username as subject

        return {"token": token}    # Return the access token
