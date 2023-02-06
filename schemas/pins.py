from pydantic import BaseModel

from schemas.base import BaseCreateSchema, BaseResponseSchema

class PinCreateSchema(BaseCreateSchema):
    longitude: float
    latitude: float


class PinResponseSchema(BaseResponseSchema):
    longitude: float
    latitude: float

    class Config:
        orm_mode = True

