import logging
from fastapi.testclient import TestClient

from manage import app

from tests.managers.pin import PinManager
from tests.managers.user import UserManager

test_client = TestClient(app)

logger = logging.getLogger(__name__)


def test_create_pins():
    with UserManager(client=test_client) as user:
        user_id = user.json().get("id")
        logger.warning("user_id: " + str(user_id))

        with PinManager(client=test_client, user_id=user_id) as pin:
            pin_body = pin.json()
            logger.warning("pin_id: " + str(pin_body.get(id)))

            assert type(pin_body.get("id")) == int


def test_read_pins():
    with UserManager(client=test_client) as user:
        user_id = user.json().get("id")
        logger.warning("user_id: " + str(user_id))

        with PinManager(client=test_client, user_id=user_id) as pin:
            pin_body = pin.json()
            pin_id = pin_body.get("id")
            logger.warning("pin_id: " + str(pin_id))

            get_response = test_client.get(f"/pins/{pin_id}").json()

            assert pin_body.get("id") == get_response.get("id")
            assert pin_body.get("description") == get_response.get("description")
