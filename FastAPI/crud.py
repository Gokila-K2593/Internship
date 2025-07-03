from fastapi import APIRouter, Depends, Query, HTTPException
from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import Annotated, Optional
from database import engine

crud_router = APIRouter()    # Create an API router


# Define Hero table model
class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)  # Auto-increment primary key
    name: str
    age: int
    secret_name: str

# Model for PATCH request (age update)
class HeroUpdate(SQLModel):
    age: Optional[int] = None

# Dependency function to create DB session
def get_session():
    with Session(engine) as session:
        yield session

# Annotated session dependency (shortcut style)
SessionDep = Annotated[Session, Depends(get_session)]

# POST Method 

@crud_router.post('/post_method/', response_model=Hero)     # Add new hero to the database
def create_hero(hero: Hero, session: Session = Depends(get_session)):
    session.add(hero)          # Add new hero to session
    session.commit()           # Save changes to DB
    session.refresh(hero)      # Refresh instance with DB values
    return hero                # Return newly created hero

#  GET Method 

@crud_router.get("/get_method/")    # Get list of heroes with optional offset and limit
def read_heroes(
    session: SessionDep,
    offset: int = 0,   # Starting point for results
    limit: Annotated[int, Query(le=100)] = 100,  # Max 100 records
) -> list[Hero]:
    # Execute SELECT query with offset and limit
    heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
    return heroes

# PUT Method

@crud_router.put("/put_method/{hero_id}", response_model=Hero)  # Update full hero details using ID
def update_hero(
    hero_id: int,
    hero: Hero,
    session: Session = Depends(get_session)
):
    
    existing_hero = session.get(Hero, hero_id)    # Get hero from DB by ID
    if existing_hero is None:
        raise HTTPException(status_code=404, detail="Hero not found")

    
    existing_hero.name = hero.name     # Update fields with new values
    existing_hero.age = hero.age
    existing_hero.secret_name = hero.secret_name

    session.commit()               
    session.refresh(existing_hero) 
    return existing_hero           

# DELETE Method

@crud_router.delete("/delete_method/{hero_id}")    # Delete a hero from the DB using ID
def delete_hero(hero_id: int, session: Session = Depends(get_session)):
    
    existing_hero = session.get(Hero, hero_id)     # Find hero in DB
    if existing_hero is None:
        raise HTTPException(status_code=404, detail="Hero not found")

    session.delete(existing_hero)  
    session.commit()            
    return {"message": f"Hero {hero_id} has been deleted successfully."}

#  PATCH Method 

@crud_router.patch("/patch_method/{hero_id}", response_model=Hero)     # Partially update hero 
def patch_hero(
    hero_id: int,
    hero_update: HeroUpdate,
    session: Session = Depends(get_session)):
    
    db_hero = session.get(Hero, hero_id)     # Get hero by ID
    if not db_hero:
        raise HTTPException(status_code=404, detail="Hero not found")

    hero_data = hero_update.dict(exclude_unset=True)    # Convert only the provided fields to dict

    for key, value in hero_data.items():      # Update only the fields that are present in request
        setattr(db_hero, key, value)  # Set new value

    session.add(db_hero)     
    session.commit()        
    session.refresh(db_hero) 
    return db_hero           

