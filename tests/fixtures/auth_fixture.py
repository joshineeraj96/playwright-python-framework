import pytest

from api.client.auth_client import AuthClient
from test_data import auth_data


@pytest.fixture(scope="session")
def auth_token(api_context):
    auth_client = AuthClient(api_context)

    response = auth_client.generate_token(auth_data.AUTH_PAYLOAD)

    assert response.status == 200
    
    response_body = response.json()

    return response_body["token"]
