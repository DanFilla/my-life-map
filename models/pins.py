from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import mapped_column, relationship

from models.base import Base


class PinModel(Base):
    __tablename__ = "pins"

    longitude = mapped_column(DECIMAL(8, 5))
    latitude = mapped_column(DECIMAL(8, 5))
    user_id = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    # relationships
    user = relationship("UserModel", back_populates="pins")
