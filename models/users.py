from sqlalchemy import Column, Integer, String

from models.base import Base

class UserModel(Base):
    __tablename__ = "users"
    
    description = Column(String(256))
