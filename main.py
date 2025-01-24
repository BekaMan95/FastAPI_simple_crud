from fastapi import FastAPI
import schema
from database import engine
from routers import user_router, post_router

app = FastAPI()
schema.Base.metadata.create_all(bind=engine)

app.include_router(user_router, prefix="/api")
app.include_router(post_router, prefix="/api")


@app.get('/')
async def root():
    return {
        "message": "Hey There!",
        "status": "success"
    }
