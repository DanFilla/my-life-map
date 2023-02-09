from tests.managers.base import BaseManager

class PinManager(BaseManager):
    def __init__(self, longitude, latitude, client, **kwargs):
        self.longitude = longitude
        self.latitude = latitude
        self.kwargs = kwargs
        super().__init__(client)

    def __enter__(self):
        self.response = self.client.post("/pins", json={"longitude": self.longitude, "latitude": self.latitude} | self.kwargs)
        return self.response


    def __exit__(self, exc_type,exc_value, exc_traceback):
        pass

