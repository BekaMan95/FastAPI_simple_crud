from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str
    user_id: int