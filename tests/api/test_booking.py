import allure
import pytest

from api.client.booking_client import BookingClient
from test_data import booking_data
from utils.schema_validator import validate_schema
from utils import fake_data_generator


class TestBooking:

    @pytest.mark.regression
    @allure.feature("Booking")
    @allure.title("Verify all bookings can be fetched")
    def test_get_all_bookings(self, api_context):

        booking_client = BookingClient(api_context)

        response = booking_client.get_all_bookings()
        assert response.status == 200

        response_body = response.json()
        assert isinstance(response_body, list)
        assert len(response_body) > 0

    
    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.feature("Booking")
    @allure.title("Verify bookings can be fetched with booking id")
    def test_get_booking_by_id(self, api_context, created_booking):

        booking_client = BookingClient(api_context)

        booking_id = created_booking["bookingid"]

        response = booking_client.get_booking(booking_id)
        assert response.status == 200

        response_body = response.json()
        assert response_body["firstname"]
        assert response_body["lastname"]
        assert response_body["bookingdates"]

        validate_schema(response_body, "booking_schema.json")



    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.feature("Booking")
    @allure.title("Verify booking can be made")
    def test_create_booking(self, api_context):

       booking_client = BookingClient(api_context)
       
       payload = fake_data_generator.generate_booking_data()

       response = booking_client.create_booking(payload)


       assert response.status == 200

       response_body = response.json()

       assert response_body["bookingid"] is not None
       assert response_body["booking"]["firstname"] == payload["firstname"]
       assert response_body["booking"]["lastname"] == payload["lastname"]
       assert response_body["booking"]["totalprice"] == payload["totalprice"]
       assert response_body["booking"]["depositpaid"] == payload["depositpaid"]
       assert response_body["booking"]["bookingdates"] == payload["bookingdates"]
       assert response_body["booking"]["additionalneeds"] == payload["additionalneeds"]


    @pytest.mark.regression
    @allure.feature("Booking")
    @allure.title("Verify booking can be updated")
    def test_update_booking(self, api_context, auth_token, created_booking):

       booking_id = created_booking["bookingid"]

       booking_client = BookingClient(api_context)

       response = booking_client.update_booking(booking_id, booking_data.UPDATE_BOOKING, auth_token)

       assert response.status == 200

       response_body = response.json()

       assert response_body["firstname"] == booking_data.UPDATE_BOOKING["firstname"]
       assert response_body["lastname"] == booking_data.UPDATE_BOOKING["lastname"]
       assert response_body["totalprice"] == booking_data.UPDATE_BOOKING["totalprice"]
       assert response_body["depositpaid"] == booking_data.UPDATE_BOOKING["depositpaid"]
       assert response_body["additionalneeds"] == booking_data.UPDATE_BOOKING["additionalneeds"]

    
    @pytest.mark.regression
    @allure.feature("Booking")
    @allure.title("Verify booking can be partially updated")
    def test_patch_booking(self, api_context, auth_token, created_booking):

       booking_id = created_booking["bookingid"]

       booking_client = BookingClient(api_context)

       response = booking_client.patch_booking(booking_id, booking_data.PATCH_BOOKING, auth_token)

       assert response.status == 200

       response_body = response.json()

       assert response_body["firstname"] == booking_data.PATCH_BOOKING["firstname"]
    

    @pytest.mark.regression
    @allure.feature("Booking")
    @allure.title("Verify booking can be deleted")
    def test_delete_booking(self, api_context, auth_token, created_booking):

       booking_id = created_booking["bookingid"]

       booking_client = BookingClient(api_context)

       response = booking_client.delete_booking(booking_id, auth_token)

       assert response.status == 200


    @pytest.mark.regression
    @allure.feature("Booking")
    @allure.title("Verify booking cannot be retrieved with invalid booking id")
    def test_get_booking_with_invalid_id(self, api_context):

        booking_client = BookingClient(api_context)

        response = booking_client.get_booking(999999)
        assert response.status == 404


    @pytest.mark.regression
    @allure.feature("Booking")
    @allure.title("Verify booking cannot be updated without authentication")
    def test_update_booking_without_token(self, api_context, created_booking):

       booking_id = created_booking["bookingid"]

       booking_client = BookingClient(api_context)

       response = booking_client.update_booking(booking_id, booking_data.UPDATE_BOOKING, "")

       assert response.status == 403


    @pytest.mark.regression
    @allure.feature("Booking")
    @allure.title("Verify booking cannot be created with invalid payload")
    def test_create_booking_with_invalid_payload(self, api_context):

        booking_client = BookingClient(api_context)

        response = booking_client.create_booking(booking_data.INVALID_BOOKING)

        assert response.status in [400, 500]