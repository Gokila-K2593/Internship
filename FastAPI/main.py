from fastapi import FastAPI, Depends,Query,HTTPException
from sqlmodel import SQLModel, Field, create_engine, Session,select
from typing import Annotated,Optional
app = FastAPI()
postgres_url = "postgresql://gokila:goki@localhost:5432/fastapi_db"
engine = create_engine(postgres_url, echo=True)
class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)  
    name: str
    age: int
    secret_name: str 
class HeroUpdate(SQLModel):
    age: Optional[int] = None
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)
def get_session():
    with Session(engine) as session:
        yield session
SessionDep = Annotated[Session, Depends(get_session)]
@app.post('/heroes/', response_model=Hero)
def create_hero(hero: Hero, session: Session = Depends(get_session)):
    session.add(hero)
    session.commit()  
    session.refresh(hero)  
    return hero  
@app.get("/heroes/")
def read_heroes(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Hero]:
    heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
    return heroes
@app.put("/heroes/{hero_id}", response_model=Hero)
def update_hero(
    hero_id: int,
    hero: Hero,
    session: Session = Depends(get_session)
):
    existing_hero = session.get(Hero, hero_id)
    if existing_hero is None:
        raise HTTPException(status_code=404, detail="Hero not found")
    existing_hero.name = hero.name
    existing_hero.age = hero.age
    existing_hero.secret_name = hero.secret_name
    session.commit()
    session.refresh(existing_hero)   
    return existing_hero
@app.delete("/heroes/{hero_id}")
def delete_hero(hero_id: int, session: Session = Depends(get_session)):
    existing_hero = session.get(Hero, hero_id)
    if existing_hero is None:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(existing_hero)
    session.commit()
    return {"message": f"Hero {hero_id} has been deleted successfully."}
@app.patch("/heroes/{hero_id}", response_model=Hero)
def patch_hero(
    hero_id: int,
    hero_update:HeroUpdate,
    session: Session = Depends(get_session)):
    db_hero = session.get(Hero, hero_id)
    if not db_hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    hero_data = hero_update.dict(exclude_unset=True)
    for key, value in hero_data.items():
        setattr(db_hero, key, value)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero