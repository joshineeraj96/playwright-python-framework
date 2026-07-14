import allure

from api.client.auth_client import AuthClient
from test_data import auth_data

class TestAuth:

    @allure.feature("Authentication")
    @allure.title("Verify token can be generated with valid credentials")
    def test_auth(self, api_context):
        auth_client = AuthClient(api_context)
        response = auth_client.generate_token(auth_data.AUTH_PAYLOAD)

        assert response.status == 200
        response_body = response.json()

        assert "token" in response_body
        assert response_body["token"]


    @allure.feature("Authentication")
    @allure.title("Verify token is not generated with invalid credentials")
    def test_auth_with_invalid_credentials(self, api_context):
        auth_client = AuthClient(api_context)
        response = auth_client.generate_token(auth_data.INVALID_AUTH_PAYLOAD)

        assert response.status == 200
        response_body = response.json()

        assert "token" not in response_body
        assert response_body["reason"] == "Bad credentials"