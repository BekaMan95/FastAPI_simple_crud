from fastapi import APIRouter, HTTPException, status
from models import UserBase
import schema
from auth import bcrypt_context
from database import db_dependency
from auth import auth_dependency

router = APIRouter()


@router.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    duplicate_user = db.query(schema.User).filter(schema.User.username == user.username).first()

    if duplicate_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"username already taken!")
    
    db_user = schema.User(
        username = user.username,
        password = bcrypt_context.hash(user.password)
    )
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
    return {
        "id": user.id,
        "username": user.username
    }

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
    return [{"id": user.id, "username": user.username} for user in users]

