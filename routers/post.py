from fastapi import APIRouter, HTTPException, status
from models import PostBase
import schema
from database import db_dependency
from auth import auth_dependency

router = APIRouter()

@router.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: PostBase, Auth: auth_dependency, db: db_dependency):
    post = post.model_dump()
    post['user_id'] = Auth['id']
    db_post = schema.Post(**post)
    db.add(db_post)
    db.commit()
    return {
        "detail": "post created!"
    }



@router.get("/posts/{id}", status_code=status.HTTP_200_OK)
async def get_post(id, db: db_dependency):
    post = db.query(schema.Post).filter(schema.Post.id == id).first()

    if post is None:
        raise HTTPException(status_code=404, detail=f"post with id {id} not found!")
    return post



@router.delete("/posts/{id}")
async def delete_post(id: int, db: db_dependency):
    db_post = db.query(schema.Post).filter(schema.Post.id == id).first()

    if db_post is None:
        raise HTTPException(status_code=404, detail=f"post with id {id} not found!")
    
    db.delete(db_post)
    db.commit()
    return {
        "detail": "post deleted successfuly!"
    }



@router.get("/posts", status_code=status.HTTP_200_OK)
async def get_posts(db: db_dependency):
    posts = db.query(schema.Post).all()
    return posts

