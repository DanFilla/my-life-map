import logging

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from schemas.users import UserResponseSchema, UserCreateSchema
from services.users import UserService
from models.users import UserModel

from libs.db import get_db

logger = logging.getLogger(__name__)

users_api_router = APIRouter()

user_service = UserService(model=UserModel)


@users_api_router.post("/users", response_model=UserResponseSchema)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    return user_service.create_one(create_schema=user, db=db)

@users_api_router.get("/users/{user_id}", response_model=UserResponseSchema)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.get_one_by_id(id=user_id, db=db)

@users_api_router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_service.delete_one_by_id(id=user_id, db=db)

