from fastapi import APIRouter, HTTPException, status
from models import UserBase
import schema
from database import db_dependency

router = APIRouter()


@router.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    db_user = schema.User(**user.dict())
    db.add(db_user)
    db.commit()
    return {
        "detail": "user created!"
    }

@router.get("/users/{id}", status_code=status.HTTP_200_OK)
async def get_user(id: int, db: db_dependency):
    user = db.query(schema.User).filter(schema.User.id == id).first()

    if user is None:
        raise HTTPException(status_code=404, detail=f"user with id {id} not found!")
    return user

@router.put("/users/{id}", status_code=status.HTTP_200_OK)
async def delete_user(id: int, user: UserBase, db: db_dependency):
    db_user = db.query(schema.User).filter(schema.User.id == id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail=f"user with id {id} not found!")
    
    for key, value in user.dict(exclude_unset=True).items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return {
        "detail": "user updated!"
    }


@router.delete("/users/{id}", status_code=status.HTTP_200_OK)
async def delete_user(id: int, db: db_dependency):
    db_user = db.query(schema.User).filter(schema.User.id == id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail=f"user with id {id} not found!")
    
    db.delete(db_user)
    db.commit()
    return {
        "detail": "user deleted!"
    }

@router.get("/users", status_code=status.HTTP_200_OK)
async def get_users(db: db_dependency):
    users = db.query(schema.User).all()
    return users

