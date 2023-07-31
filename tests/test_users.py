import logging
import pytest
from fastapi.testclient import TestClient

from contextlib import contextmanager
from manage import app
from libs.db import get_db

from tests.managers.user import UserManager

from models.users import UserModel

test_client = TestClient(app)

logger = logging.getLogger(__name__)

def test_create_and_delete_users():
    with UserManager(client=test_client) as user:
        user_body = user.json()

        logger.debug(user_body.get("id"))
        user_id = user_body.pop("id")

        assert type(user_id) == int
        assert user_body == UserManager.DEFAULT_USER_KWARGS

    with contextmanager(get_db)() as db:
        if db.query(UserModel).filter(UserModel.id == user_id).first():
            pytest.fail('User was not deleted')


def test_read_users():
    with UserManager(client=test_client) as user:
        user_body = user.json()
        user_id = user_body.get("id")

        get_response = test_client.get(f"/users/{user_id}").json()

        assert user_body.get("id") == get_response.get("id")
        assert user_body.get("description") == get_response.get("description")
