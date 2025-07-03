from fastapi import Depends, HTTPException, Security,APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, APIKeyHeader
from jose import jwt, JWTError
from datetime import datetime, timedelta
from sqlmodel import SQLModel, Field, Session, create_engine, select
from typing import Optional
from database import engine

# Create FastAPI router instance for auth module
auth_router = APIRouter()


class Auth(SQLModel, table=True):     # Table to store user credentials
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str

SECRET_KEY = "secret123"          # Used to encode and decode the JWT
ALGORITHM = "HS256"               # JWT algorithm
EXPIRY_MINUTES = 30               # Token expiry time

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")    # OAuth2 scheme to read token from the request
api_key_scheme = APIKeyHeader(name="Authorization")    # To extract token from the Authorization header


def get_session():      # Function to create DB session for each request
    with Session(engine) as session:
        yield session


def create_access_token(data: dict):     # Create a JWT token for the given user data
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=EXPIRY_MINUTES)
    to_encode.update({"exp": expire})  # Add expiry time to token
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str):    # Decode and verify the token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload  # Return decoded data if valid
    except JWTError:    # Return None if invalid
        return None     


@auth_router.post("/signup")    # Register new user with username and password
def signup(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session)):
    # Check if user already exists in the DB
    user_exists = session.exec(
        select(Auth).where(Auth.username == form_data.username)).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Username already exists")

    new_user = Auth(username=form_data.username, password=form_data.password)     # Create and save new user to DB
    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return {"message": f"User '{new_user.username}' created successfully"}


@auth_router.post("/login")     # Authenticate user and return JWT token
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session)):
    # Check if username & password match
    user = session.exec(
        select(Auth).where(
            (Auth.username == form_data.username) & 
            (Auth.password == form_data.password))).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.username})     # Create token for the user

    return {"access_token": token, "token_type": "bearer"}



@auth_router.get("/protected")     # Only allow access if valid token is passed
def protected(api_key: str = Security(api_key_scheme)):
    
    if not api_key.startswith("Bearer "):     # Token should be in "Bearer <token>" format
        raise HTTPException(status_code=401, detail="Token missing or invalid")

    token = api_key[len("Bearer "):]   # Remove "Bearer " from the token string

    user_data = verify_token(token)    # Verify the token
    if user_data is None:
        raise HTTPException(status_code=401, detail="Token invalid or expired")

    return {"message": f"Welcome {user_data['sub']}! You are logged in!"}     # Return welcome message with username
