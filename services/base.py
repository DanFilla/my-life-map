import logging
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from typing import TypeVar, Generic, Type
from sqlalchemy.orm import Session
from sqlalchemy import delete

from schemas.base import BaseCreateSchema

from models.base import Base

logger = logging.getLogger(__name__)

CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseCreateSchema)
ModelType = TypeVar("ModelType", bound=Base)


class BaseService(Generic[ModelType, CreateSchemaType]):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_one_by_id(self, id: int, db: Session):
        retrived_resource = db.query(self.model).filter(self.model.id == id).first()
        if retrived_resource:
            return retrived_resource
        else:
            raise HTTPException(status_code=404, detail="resource not found")

    def create_one(self, create_schema: CreateSchemaType, db: Session, *args, **kwargs):
        encoded_create_schema = jsonable_encoder(create_schema)
        create_object = self.model(**encoded_create_schema)

        db.add(create_object)
        db.commit()

        db.refresh(create_object)
        return create_object

    def delete_one_by_id(self, id: int, db: Session):
        retrived_resource = db.query(self.model).filter(self.model.id == id).first()

        if retrived_resource:
            db.delete(retrived_resource)
            db.commit()

