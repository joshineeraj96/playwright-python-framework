import allure
import pytest

from api.client.auth_client import AuthClient
from test_data import auth_data

class TestAuth:

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.feature("Authentication")
    @allure.title("Verify token can be generated with valid credentials")
    def test_auth(self, api_context):
        auth_client = AuthClient(api_context)
        response = auth_client.generate_token(auth_data.AUTH_PAYLOAD)

        assert response.status == 200
        response_body = response.json()

        assert "token" in response_body
        
        # this is to test the response time
        # assert response.timing["responseEnd"] < 1000
        assert isinstance(response_body["token"], str)
        assert len(response_body["token"]) > 0



    @pytest.mark.regression
    @allure.feature("Authentication")
    @allure.title("Verify token is not generated with invalid credentials")
    def test_auth_with_invalid_credentials(self, api_context):
        auth_client = AuthClient(api_context)
        response = auth_client.generate_token(auth_data.INVALID_AUTH_PAYLOAD)

        assert response.status == 200
        response_body = response.json()

        assert "token" not in response_body
        assert response_body["reason"] == "Bad credentials"