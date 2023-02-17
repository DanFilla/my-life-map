import logging

from fastapi import HTTPException
from sqlalchemy.orm import Session

from schemas.pins import PinCreateSchema
from models.pins import PinModel

from services.base import BaseService

logger = logging.getLogger(__name__)


class PinService(BaseService[PinModel, PinCreateSchema]):
    def create_one(self, create_schema: PinCreateSchema, db: Session, *args, **kwargs):
        if abs(create_schema.longitude) > 180 or abs(create_schema.latitude) > 180:
            raise HTTPException(
                status_code=422, detail="improper format for coordinates"
            )

        return super().create_one(create_schema=create_schema, db=db)
