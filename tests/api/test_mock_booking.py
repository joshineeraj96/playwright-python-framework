import allure

from api.client.booking_client import BookingClient


class TestMockBooking:

    @allure.feature("WireMock")
    @allure.title("Verify booking can be fetched from WireMock")
    def test_get_booking_from_mock_server(self, mock_api_context):

        booking_client = BookingClient(mock_api_context)

        response = booking_client.get_booking(1)

        assert response.status == 200

        response_body = response.json()

        assert response_body["firstname"] == "Neeraj"
        assert response_body["lastname"] == "Joshi"
        assert response_body["totalprice"] == 500
        assert response_body["depositpaid"] is True
        assert response_body["bookingdates"]["checkin"] == "2026-07-15"
        assert response_body["bookingdates"]["checkout"] == "2026-07-20"
        assert response_body["additionalneeds"] == "Breakfast"