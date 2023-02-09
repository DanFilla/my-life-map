from tests.managers.base import BaseManager

class UserManager(BaseManager):
    def __init__(self, description, client):
        self.description = description
        self.user_id = None
        super().__init__(client)

    def __enter__(self):
        self.response = self.client.post("/users", json={"description": self.description})
        self.user_id = self.response.json().get('id')
        return self.response


    def __exit__(self, exc_type,exc_value, exc_traceback):
        self.client.delete(f"/users/{self.user_id}")

