from sqlalchemy import Column, Integer, String

from models.base import Base

class User(Base):
    __tablename__ = "users"
    
    description = Column(String(256))
