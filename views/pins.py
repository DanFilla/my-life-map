import logging

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from schemas.pins import PinResponseSchema, PinCreateSchema
from services.pins import PinService
from models.pins import PinModel

from libs.db import get_db

logger = logging.getLogger(__name__)

pins_api_router = APIRouter()

pin_service = PinService(model=PinModel)


@pins_api_router.post("/pins", response_model=PinResponseSchema)
def create_pin(pin: PinCreateSchema, db: Session = Depends(get_db)):
    return pin_service.create_one(create_schema=pin, db=db)


@pins_api_router.get("/pins/{pin_id}", response_model=PinResponseSchema)
def get_pin(pin_id: int, db: Session = Depends(get_db)):
    return pin_service.get_one_by_id(id=pin_id, db=db)


@pins_api_router.delete("/pins/{pin_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pin(pin_id: int, db: Session = Depends(get_db)):
    pin_service.delete_one_by_id(id=pin_id, db=db)
