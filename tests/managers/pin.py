from tests.managers.base import BaseManager


class PinManager(BaseManager):
    DEFAULT_PIN_KWARGS = {
        "longitude": 123.123456,
        "latitude": 12.185,
    }

    def __init__(self, client, user_id, pin_kwargs=None):
        self.pin_kwargs = pin_kwargs if pin_kwargs else self.DEFAULT_PIN_KWARGS
        self.pin_kwargs["user_id"] = user_id
        super().__init__(client)

    def __enter__(self):
        self.response = self.client.post("/pins", json=self.pin_kwargs)

        self.pin_id = self.response.json().get("id")

        return self.response

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.client.delete(f"/pins/{self.pin_id}")
