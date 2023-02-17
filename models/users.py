from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship

from models.base import Base

class UserModel(Base):
    __tablename__ = "users"
    
    first_name = mapped_column(String(50))
    last_name = mapped_column(String(50))
    email = mapped_column(String(100), nullable=False, default="come@mebro.com")
    user_name = mapped_column(String(50), nullable=False, default="default")
    description = mapped_column(String(256))

    #relationships
    pins = relationship("PinModel")
