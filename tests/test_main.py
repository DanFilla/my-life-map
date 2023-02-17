import logging
from fastapi.testclient import TestClient

from manage import app

from tests.managers.user import UserManager

test_client = TestClient(app)

logger = logging.getLogger(__name__)
