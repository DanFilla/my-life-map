import os 
import logging
import boto3
import pytest
from botocore.exceptions import ClientError

from fastapi.testclient import TestClient
from contextlib import contextmanager
from libs.db import get_db

from manage import app

from tests.managers.audio_clips import AudioClipsManager
from tests.managers.user import UserManager

from models.audio_clips import AudioClipModel

test_client = TestClient(app)

logger = logging.getLogger(__name__)

bucket_name = os.environ.get('BUCKET_NAME')
region = os.environ.get('REGION')
base_url = f'https://{bucket_name}.s3.{region}.amazonaws.com'
s3 = boto3.client('s3', aws_access_key_id=os.environ.get('ACCESS_KEY'), aws_secret_access_key=os.environ.get('SECRET_KEY'))

def test_create_and_delete_audio_clips():

    g_audio_clip_key:int

    with UserManager(client=test_client) as user:
        user_id = user.json().get("id")
        logger.warning("user_id: " + str(user_id))

        with AudioClipsManager(audio_clip_file_path='tests/static/Test_Audio_File.m4a', client=test_client, user_id=user_id) as audio_clip:
            audio_clip_body = audio_clip.json()
            logger.warning("audio_clip_id: " + str(audio_clip_body))

            g_audio_clip_key = audio_clip_body.get('file_key')

            assert type(audio_clip_body.get("id")) == int
            assert audio_clip_body.get("file_key") == 'Test_Audio_File.m4a'

    # Audio Clip was deleted from s3
    try:
        s3.get_object(Bucket='audio-samples-df', Key=g_audio_clip_key)
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            logger.info('s3 object was deleted.')
        else:
            pytest.fail('Audio clip was not deleted from s3')

    # Audio Clip was deleted form db
    with contextmanager(get_db)() as db:
        if db.query(AudioClipModel).filter(AudioClipModel.id == user_id).first():
            pytest.fail('Audio Clip was not deleted from db')

def test_read_audio_clips():
    with UserManager(client=test_client) as user:
        user_id = user.json().get("id")
        logger.warning("user_id: " + str(user_id))

        with AudioClipsManager(audio_clip_file_path='tests/static/Test_Audio_File.m4a', client=test_client, user_id=user_id) as audio_clip:
            audio_clip_body = audio_clip.json()
            response = test_client.get(f"/audio_clips/{audio_clip_body['id']}").json()

            assert audio_clip_body.get("id") == response.get("id")
            assert user_id == response.get("creator_id")
            assert audio_clip_body.get("file_key") == 'Test_Audio_File.m4a'

