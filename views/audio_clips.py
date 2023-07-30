import logging

from fastapi import APIRouter, Depends, status, UploadFile, File
from sqlalchemy.orm import Session

from schemas.audio_clips import AudioClipCreateSchema, AudioClipResponseSchema
from services.audio_clips import AudioClipService
from models.audio_clips  import AudioClipModel
from fastapi import UploadFile, File, Form

from libs.db import get_db

logger = logging.getLogger(__name__)

audio_clips_api_router = APIRouter()

audio_clips_service = AudioClipService(model=AudioClipModel)

@audio_clips_api_router.post("/audio_clips")
def create_audio_clips(file: UploadFile = File(...), user_id: int = Form(...), db: Session = Depends(get_db)):
    return audio_clips_service.no_schema_create_one(file=file, db=db, model_args={'creator_id': user_id})


@audio_clips_api_router.get("/audio_clips/{audio_clip_id}", response_model=AudioClipResponseSchema)
def get_audio_clips(audio_clip_id: int, db: Session = Depends(get_db)):
    return audio_clips_service.get_one_by_id(id=audio_clip_id, db=db)


@audio_clips_api_router.delete("/audio_clips/{audio_clip_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_audio_clips(audio_clip_id: int, db: Session = Depends(get_db)):
    audio_clips_service.delete_one_by_id(id=audio_clip_id, db=db)
