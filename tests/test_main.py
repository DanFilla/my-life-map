import logging
from fastapi.testclient import TestClient

from manage import app

from tests.managers.user import UserManager

test_client = TestClient(app)

logger = logging.getLogger(__name__)

def test_create_users():
    with UserManager(test_client) as user:
        user_body = user.json()

        assert type(user_body.get('id')) == int


def test_read_users():
    with UserManager(test_client) as user:
        user_body = user.json()

        get_response = test_client.get(f"/users/{user_body.get('id')}").json()

        assert user_body.get('id') == get_response.get('id')
        assert user_body.get('description') == get_response.get('description')

