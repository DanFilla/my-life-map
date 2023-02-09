import logging

from fastapi import HTTPException
from sqlalchemy.orm import Session

from schemas.pins import PinCreateSchema
from models.pins import Pin

from services.base import BaseService

logger = logging.getLogger(__name__)

class PinService(BaseService[Pin, PinCreateSchema]):

    def get_one_by_id(self, pin_id: int, db: Session, *args, **kwargs):
        return super().get_one_by_id(id=pin_id, db=db)
    
    def create_one(self, pin: PinCreateSchema, db: Session, *args, **kwargs):
        if abs(pin.longitude) > 180 or abs(pin.latitude) > 180:
            raise HTTPException(status_code=422, detail="improper format for coordinates")

        return super().create_one(create_schema=pin, db=db)

