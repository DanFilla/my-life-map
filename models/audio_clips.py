from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import mapped_column, relationship

from models.base import Base


class AudioClipModel(Base):
    __tablename__ = "audio_samples"

    s3_url = mapped_column(String(255), nullable=False)
    file_key = mapped_column(String(255), nullable=False)
    creator_id = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    # relationships
    user = relationship("UserModel", back_populates="audio_clips")

