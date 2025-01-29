from datetime import timedelta, datetime
from fastapi import HTTPException, APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from typing import Annotated
from database import db_dependency
from models.user import UserBase
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
import schema
from config import SECRET_KEY, ALGORITHM

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='/api/auth/login')

class CreateUserRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

@router.post("/login", response_model=Token)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], 
    db: db_dependency
    ):
    user = authenticate_user(form_data.username, form_data.password, db)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect credentials!")

    token = create_access_token(user.username, user.id, timedelta(minutes=60))

    return {
        "access_token": token,
        "token_type": "bearer"
    }


def authenticate_user(username: str, password: str, db):
    user = db.query(schema.User).filter(schema.User.username == username).first()
    if not user or not bcrypt_context.verify(password, user.password):
        return False

    return user

def create_access_token(username: str, id: int, exp_delta: timedelta):
    expires = datetime.utcnow() + exp_delta
    encoded_info = {"sub": username, "id": id, "exp": expires}

    return jwt.encode(encoded_info, SECRET_KEY, algorithm=ALGORITHM)
    

async def authenticate(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)

        id: int =  payload.get("id")
        username: str = payload.get("sub")
        if id == None or username == None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid user!")
        
        return {
            "id": id,
            "username": username
        }
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user!")


auth_dependency = Annotated[dict, Depends(authenticate)]
