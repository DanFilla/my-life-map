from tests.managers.base import BaseManager

class PinManager(BaseManager):
    def __init__(self, longitude, latitude, client, **kwargs):
        self.longitude = longitude
        self.latitude = latitude
        self.kwargs = kwargs
        self.pin_id = None
        super().__init__(client)

    def __enter__(self):
        self.response = self.client.post("/pins", json={"longitude": self.longitude, "latitude": self.latitude} | self.kwargs)

        self.pin_id = self.response.json().get('id')

        return self.response


    def __exit__(self, exc_type,exc_value, exc_traceback):
        self.client.delete(f"/pins/{self.pin_id}")

