from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class PostBase(BaseModel):
    title: str
    content: str
    user_id: int

class UserBase(BaseModel):
    username: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]



@app.get('/')
async def root():
    return {
        "message": "Hey There!",
        "status": "success"
    }


@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    return {
        "detail": "user created!"
    }

@app.get("/users/{id}", status_code=status.HTTP_200_OK)
async def get_user(id: int, db: db_dependency):
    user = db.query(models.User).filter(models.User.id == id).first()

    if user is None:
        raise HTTPException(status_code=404, detail=f"user with id {id} not found!")
    return user

@app.put("/users/{id}", status_code=status.HTTP_200_OK)
async def delete_user(id: int, user: UserBase, db: db_dependency):
    db_user = db.query(models.User).filter(models.User.id == id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail=f"user with id {id} not found!")
    
    for key, value in user.dict(exclude_unset=True).items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return {
        "detail": "user updated!"
    }


@app.delete("/users/{id}", status_code=status.HTTP_200_OK)
async def delete_user(id: int, db: db_dependency):
    db_user = db.query(models.User).filter(models.User.id == id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail=f"user with id {id} not found!")
    
    db.delete(db_user)
    db.commit()
    return {
        "detail": "user deleted!"
    }

@app.get("/users", status_code=status.HTTP_200_OK)
async def get_users(db: db_dependency):
    users = db.query(models.User).all()
    return users


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: PostBase, db: db_dependency):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    return {
        "detail": "post created!"
    }

@app.get("/posts/{id}", status_code=status.HTTP_200_OK)
async def get_post(id, db: db_dependency):
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if post is None:
        raise HTTPException(status_code=404, detail=f"post with id {id} not found!")
    return post

@app.delete("/posts/{id}")
async def delete_post(id: int, db: db_dependency):
    db_post = db.query(models.Post).filter(models.Post.id == id).first()

    if db_post is None:
        raise HTTPException(status_code=404, detail=f"post with id {id} not found!")
    
    db.delete(db_post)
    db.commit()
    return {
        "detail": "post deleted successfuly!"
    }

@app.get("/posts", status_code=status.HTTP_200_OK)
async def get_posts(db: db_dependency):
    posts = db.query(models.Post).all()
    return posts

