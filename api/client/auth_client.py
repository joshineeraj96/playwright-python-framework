from api.client.api_client import APIClient

class AuthClient(APIClient):

    def __init__(self, api_context):
        super().__init__(api_context)

    def generate_token(self, payload):
        return self.post("/auth", data=payload)
