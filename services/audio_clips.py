import logging
from urllib.parse import urlencode
from sqlalchemy.orm import Session

from services.base import BaseService
from services.s3 import S3Service
from models.audio_clips import AudioClipModel
from schemas.audio_clips import AudioClipCreateSchema

logger = logging.getLogger(__name__)

class AudioClipService(BaseService[AudioClipModel, AudioClipCreateSchema]):

    def no_schema_create_one(self, file, db: Session, model_args: dict, *args, **kwargs):
 
        model_args['file_key'] = file.filename

        model_args['s3_url'] = S3Service().upload(file_data=file.file, file_key=model_args.get('file_key'))

        return super().no_schema_create_one(db=db, model_args=model_args)

    def delete_one_by_id(self, id: int, db: Session):
        s3_url = db.query(AudioClipModel).filter(AudioClipModel.id==id).first().file_key

        S3Service().delete(s3_file_path=s3_url)

        return super().delete_one_by_id(id, db)
