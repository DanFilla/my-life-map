from pydantic import BaseModel

class UserBase(BaseModel):
    pass

class UserCreate(UserBase):
    description: str

class User(UserBase):
    id: int
    description: str

    class Config:
        orm_mode = True

