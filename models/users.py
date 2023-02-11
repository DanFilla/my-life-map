from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship

from models.base import Base

class UserModel(Base):
    __tablename__ = "users"
    
    description = mapped_column(String(256))

    #relationships
    pins = relationship("PinModel")
