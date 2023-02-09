import logging
from sqlalchemy.orm import Session

from services.base import BaseService
from schemas.users import UserCreateSchema
from models.users import UserModel

logger = logging.getLogger(__name__)

class UserService(BaseService[UserModel, UserCreateSchema]):

    def get_one_by_id(self, user_id: int, db: Session):
        return super().get_one_by_id(id=user_id, db=db)

    
    def create_one(self, user: UserCreateSchema, db: Session):
        return super().create_one(create_schema=user, db=db)

