from sqlalchemy.orm import Session

from schemas.users import UserCreateSchema
from models.users import User

class UserService:

    def get_user(self, user_id: int, db: Session):
        return db.query(User).filter(User.id == user_id).first()

    
    def create_user(self, user: UserCreateSchema, db: Session):
        db_user = User(description=user.description)
        db.add(db_user)
        db.commit()

        db.refresh(db_user)
        return db_user

