from pydantic import BaseModel

from schemas.base import BaseCreateSchema, BaseResponseSchema

class PinCreateSchema(BaseCreateSchema):
    user_id: int
    longitude: float
    latitude: float


class PinResponseSchema(BaseResponseSchema):
    user_id: int
    longitude: float
    latitude: float

    class Config:
        orm_mode = True

