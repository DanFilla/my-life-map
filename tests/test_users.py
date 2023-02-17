import logging
from fastapi.testclient import TestClient

from manage import app

from tests.managers.user import UserManager

test_client = TestClient(app)

logger = logging.getLogger(__name__)


def test_create_users():
    with UserManager(client=test_client) as user:
        user_body = user.json()

        logger.debug(user_body.get("id"))
        user_id = user_body.pop("id")

        assert type(user_id) == int
        # assert user_body.get('description') == UserManager.DEFAULT_USER_KWARGS.get('description')
        assert user_body == UserManager.DEFAULT_USER_KWARGS


def test_read_users():
    with UserManager(client=test_client) as user:
        user_body = user.json()
        user_id = user_body.get("id")

        get_response = test_client.get(f"/users/{user_id}").json()

        assert user_body.get("id") == get_response.get("id")
        assert user_body.get("description") == get_response.get("description")
