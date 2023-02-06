from pydantic import BaseModel

from schemas.base import BaseCreateSchema, BaseResponseSchema


class UserCreateSchema(BaseCreateSchema):
    description: str


class UserResponseSchema(BaseResponseSchema):
    description: str

    class Config:
        orm_mode = True

