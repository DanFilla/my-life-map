import logging
from fastapi.testclient import TestClient

from manage import app

from tests.managers.pin import PinManager

test_client = TestClient(app)

logger = logging.getLogger(__name__)

LONGITUDE = 123.123456
LATITUDE = 12.185

def test_create_pins():
    with PinManager(client=test_client, longitude=LONGITUDE, latitude=LATITUDE) as pin:
        pin_body = pin.json()

        assert type(pin_body.get('id')) == int


def test_read_users():
    with PinManager(client=test_client, longitude=LONGITUDE, latitude=LATITUDE) as pin:
        pin_body = pin.json()
        pin_id = pin_body.get('id')

        get_response = test_client.get(f"/pins/{pin_id}").json()

        assert pin_body.get('id') == get_response.get('id')
        assert pin_body.get('description') == get_response.get('description')

