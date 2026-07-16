import pytest
import base64

from api.client.auth_client import AuthClient
from test_data import auth_data


@pytest.fixture(scope="session")
def cookie_headers(api_context):
    auth_client = AuthClient(api_context)

    response = auth_client.generate_token(auth_data.AUTH_PAYLOAD)

    assert response.status == 200
    
    token = response.json()["token"]

    return {
        "Cookie": f"token={token}"
    }


# Example for APIs using HTTP Basic Authentication
@pytest.fixture(scope="session")
def basic_auth_headers():
    credentials = f"{auth_data.AUTH_PAYLOAD['username']}:{auth_data.AUTH_PAYLOAD['password']}"
    basic_auth = base64.b64encode(credentials.encode()).decode()
    return {
        "Authorization": f"Basic {basic_auth}"
    }


# Example for APIs using Bearer Token Authentication
@pytest.fixture(scope="session")
def bearer_auth_headers(api_context):
    auth_client = AuthClient(api_context)

    response = auth_client.generate_token(auth_data.AUTH_PAYLOAD)

    assert response.status == 200
    
    token = response.json()["access_token"]

    return {
        "Authorization": f"Bearer {token}"
    }