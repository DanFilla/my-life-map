from sqlalchemy import Column, Integer

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    id = Column(Integer, primary_key=True)
