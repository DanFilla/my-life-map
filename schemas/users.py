from pydantic import BaseModel

from schemas.base import BaseCreateSchema, BaseResponseSchema


class UserCreateSchema(BaseCreateSchema):
    first_name: str | None
    last_name: str | None
    email: str
    user_name: str
    description: str | None


class UserResponseSchema(BaseResponseSchema):
    first_name: str | None
    last_name: str | None
    email: str
    user_name: str
    description: str | None

    class Config:
        orm_mode = True
