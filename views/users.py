import logging

from fastapi import APIRouter, Depends
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
    return user_service.create_one(user=user, db=db)

@users_api_router.get("/users/{user_id}", response_model=UserResponseSchema)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.get_one_by_id(user_id=user_id, db=db)

