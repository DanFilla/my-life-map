import logging

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.users import User, UserCreate
from services.users import UserService

from libs.db import get_db

logger = logging.getLogger(__name__)

users_api_router = APIRouter()

user_service = UserService()


@users_api_router.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    logger.debug("Creating User")
    return user_service.create_user(user=user, db=db)

@users_api_router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.get_user(user_id=user_id, db=db)

