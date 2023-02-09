from fastapi.testclient import TestClient

class BaseManager:
    def __init__(self, client: TestClient):
        self.client = client

