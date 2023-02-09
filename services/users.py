import logging
from sqlalchemy.orm import Session

from services.base import BaseService
from schemas.users import UserCreateSchema
from models.users import UserModel

logger = logging.getLogger(__name__)

class UserService(BaseService[UserModel, UserCreateSchema]):
    pass

