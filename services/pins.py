from fastapi import HTTPException
from sqlalchemy.orm import Session

from schemas.pins import PinCreateSchema
from models.pins import Pin

class PinService:

    def get_pin(self, pin_id: int, db: Session):
        return db.query(Pin).filter(Pin.id == pin_id).first()

    
    def create_pin(self, pin: PinCreateSchema, db: Session):

        split_long = str(pin.longitude).split('.')
        longitude_whole = split_long[0]
        longitude_fractional = split_long[1]

        split_lat= str(pin.latitude).split('.')
        latitude_whole = split_lat[0]
        latitude_fractional = split_lat[1]

        if abs(pin.longitude) > 180 or abs(pin.latitude) > 180:
            pin.longitude = float(longitude_whole + longitude_fractional[:6])
            pin.latitude = float(latitude_whole + latitude_fractional[:6])

            raise HTTPException(status_code=422, detail="improper format for coordinates")

        db_pin= Pin(longitude=pin.longitude, latitude=pin.latitude)
        db.add(db_pin)
        db.commit()

        db.refresh(db_pin)
        return db_pin

