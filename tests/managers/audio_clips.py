import logging
from tests.managers.base import BaseManager

from fastapi import UploadFile

logger = logging.getLogger(__name__)

class AudioClipsManager(BaseManager):
    DEFAULT_AUDIO_CLIPS_KWARGS = None

    def __init__(self, client, user_id, audio_clip_file_path, audio_clips_kwargs=None):
        if not audio_clips_kwargs:
            audio_clips_kwargs = {}

        self.audio_clip_file_path = audio_clip_file_path
        self.file_data = {}
        self.form_data = audio_clips_kwargs 
        self.form_data["user_id"] = user_id
        super().__init__(client)

    def __enter__(self):
        with open(self.audio_clip_file_path, 'wb+') as opened_file:
            self.file_data["file"] = opened_file
            self.response = self.client.post("/audio_clips", files=self.file_data, data=self.form_data)

        logger.warning(self.response)

        self.audio_clip_id = self.response.json().get("id")

        return self.response

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.client.delete(f"/audio_clips/{self.audio_clip_id}")

