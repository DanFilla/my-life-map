import logging

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.pins import PinResponseSchema, PinCreateSchema
from services.pins import PinService

from libs.db import get_db

logger = logging.getLogger(__name__)

pins_api_router = APIRouter()

pin_service = PinService()


@pins_api_router.post("/pins", response_model=PinResponseSchema)
def create_pin(pin: PinCreateSchema, db: Session = Depends(get_db)):
    return pin_service.create_pin(pin=pin, db=db)

@pins_api_router.get("/pins/{pin_id}", response_model=PinResponseSchema)
def get_pin(pin_id: int, db: Session = Depends(get_db)):
    return pin_service.get_pin(pin_id=pin_id, db=db)

