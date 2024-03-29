from pydantic import BaseModel
from typing import Annotated

from fastapi import UploadFile, File, Form
from schemas.base import BaseCreateSchema, BaseResponseSchema


class AudioClipCreateSchema(BaseCreateSchema):
    file: UploadFile = File(...)
    user_id: int = Form(...)


class AudioClipResponseSchema(BaseResponseSchema):
    s3_url: str
    creator_id: int
    id: int
    file_key: str

    class Config:
        orm_mode = True
