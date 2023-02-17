from tests.managers.base import BaseManager

class UserManager(BaseManager):
    DEFAULT_USER_KWARGS = {
                "description": "This is a test description",
                "user_name": "test_user_name",
                "email": "come@mebro.com",
                "first_name": "Test",
                "last_name": "Me"
            }

    def __init__(self, client, user_kwargs=None):
        self.user_kwargs = user_kwargs if user_kwargs else self.DEFAULT_USER_KWARGS 
        super().__init__(client)

    def __enter__(self):

        self.response = self.client.post("/users", json=self.user_kwargs)
        self.user_id = self.response.json().get('id')
        return self.response


    def __exit__(self, exc_type,exc_value, exc_traceback):
        self.client.delete(f"/users/{self.user_id}")

