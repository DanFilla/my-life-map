from pydantic import BaseModel

class BaseCreateSchema(BaseModel):
    pass


class BaseResponseSchema(BaseModel):
    id: int
