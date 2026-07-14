import pytest

from api.client.booking_client import BookingClient
from test_data import booking_data
from utils import fake_data_generator


@pytest.fixture(scope="function")
def created_booking(api_context):

    booking_client = BookingClient(api_context)

    response = booking_client.create_booking(fake_data_generator.generate_booking_data())

    assert response.status == 200

    response_body = response.json()

    return response_body