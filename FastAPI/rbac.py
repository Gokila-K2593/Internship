from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Optional
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

rbac_router = APIRouter()          # Create an API router for RBAC related route

DATABASE_URL = "postgresql://gokila:goki@localhost:5432/fastapi_db"# PostgreSQL DB connection URL
SECRET_KEY = "your_secret_key"     # Secret key for JWT token 
ALGORITHM = "HS256"                # JWT encryption algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = 30   # Token expiry time in minutes

engine = create_engine(DATABASE_URL, echo=True)   # Create DB engine

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")    # Password hashing context using bcrypt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")     # OAuth2 token scheme (used to read token from request)

class Rbac(SQLModel, table=True):  # Table model to store user data
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    hashed_password: str
    role: str                      # Can be "admin" or "user"

class UserCreate(BaseModel):       # Input model for signup request
    username: str
    password: str
    role: str

class Token(BaseModel):            # Output model for login token response
    access_token: str
    token_type: str


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)       # Create tables in DB (run once during startup)



def get_session():           # Open DB session for each request
    with Session(engine) as session:
        yield session

def verify_password(plain_password, hashed_password):    # Compare plain password and hashed password
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):      # Hash the plain password
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = None):     # Create JWT access token with expiry
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_user_by_username(session: Session, username: str):       # Fetch user by username from DB
    statement = select(Rbac).where(Rbac.username == username)
    return session.exec(statement).first()

def authenticate_user(session: Session, username: str, password: str):    # Authenticate user credentials for login
    user = get_user_by_username(session, username)
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user

# Extract current user from token (used in protected routes)
def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Could not validate credentials",)
    try:
        # Decode JWT token and extract username
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = get_user_by_username(session, username)        # Fetch user from DB using username
    if user is None:
        raise credentials_exception
    return user


def require_role(required_role: str):          # Role-based access control function
    def role_checker(current_user: Rbac = Depends(get_current_user)):
        if current_user.role != required_role:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Only {required_role}s can access this resource")
        return current_user
    return role_checker


# Signup endpoint: Register new user
@rbac_router.post("/signup")
def signup(user: UserCreate):
    try:
       
        with Session(engine) as session:      # Start DB session

            user_in_db = session.exec(
                select(Rbac).where(Rbac.username == user.username)).first()     # Check if username already exists
            
            if user_in_db:
                raise HTTPException(status_code=400,
                    detail="Username already taken")      # If exists, raise error

            hashed = get_password_hash(user.password)         # Hash the password

            new_user = Rbac(username=user.username,
                hashed_password=hashed,
                role=user.role)    # Create new user with hashed password and role

            # Save to DB
            session.add(new_user)
            session.commit()

            # Return success message
            return {"message": "User created successfully"}

    except Exception as e:
        
        print(" Signup error:", str(e)) # Log the error and return internal server error
        raise HTTPException(status_code=500,
            detail="Internal Server Error")


@rbac_router.post("/login", response_model=Token)     # Login endpoint: Authenticate and return token
def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    # Validate username and password
    user = authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Create JWT access token with user's username as subject
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# Admin-only endpoint: Protected by admin role
@rbac_router.get("/admin-only")
def admin_route(current_user: Rbac = Depends(require_role("admin"))):
    return {"msg": f"Hello Admin {current_user.username}"}

# User-only endpoint: Protected by user role
@rbac_router.get("/user-only")
def user_route(current_user: Rbac = Depends(require_role("user"))):
    return {"msg": f"Hello User {current_user.username}"}

