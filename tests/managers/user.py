from tests.managers.base import BaseManager

class UserManager(BaseManager):

    def __enter__(self):
        self.response = self.client.post("/users", json={"description": "From testing suite"})
        return self.response


    def __exit__(self, exc_type,exc_value, exc_traceback):
        pass

