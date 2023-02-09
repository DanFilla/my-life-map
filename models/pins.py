from sqlalchemy import Column, Integer, String, DECIMAL 

from models.base import Base

class PinModel(Base):
    __tablename__ = "pins"

    longitude = Column(DECIMAL(8, 5))
    latitude = Column(DECIMAL(8, 5))

