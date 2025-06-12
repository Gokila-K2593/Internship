from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, APIKeyHeader
from jose import jwt, JWTError
from datetime import datetime, timedelta
from sqlmodel import SQLModel, Field, Session, create_engine, select
from typing import Optional
DATABASE_URL = "postgresql://gokila:goki@localhost/fastapi_db"
engine = create_engine(DATABASE_URL, echo=True)
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str 
app = FastAPI()
SECRET_KEY = "secret123"
ALGORITHM = "HS256"
EXPIRY_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
api_key_scheme = APIKeyHeader(name="Authorization")
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)
def get_session():
    with Session(engine) as session:
        yield session
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=EXPIRY_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
@app.post("/signup")
def signup(form_data: OAuth2PasswordRequestForm = Depends(),session: Session = Depends(get_session)):
    user_exists = session.exec(
        select(User).where(User.username == form_data.username)
    ).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Username already exists")
    new_user = User(username=form_data.username, password=form_data.password)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return {"message": f"User '{new_user.username}' created successfully"}
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(),
          session: Session = Depends(get_session)):
    user = session.exec(
        select(User).where(
            User.username == form_data.username,
            User.password == form_data.password
        )
    ).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
@app.get("/protected")
def protected(api_key: str = Security(api_key_scheme)):
    if not api_key.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token missing or invalid")
    token = api_key[len("Bearer "):]
    user_data = verify_token(token)
    if user_data is None:
        raise HTTPException(status_code=401, detail="Token invalid or expired")
    return {"message": f"Vanakkam {user_data['sub']}! You are logged in!"}
