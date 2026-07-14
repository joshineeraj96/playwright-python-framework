from api.client.api_client import APIClient

class BookingClient(APIClient):

    def __init__(self, api_context):
        super().__init__(api_context)


    def get_all_bookings(self):
        return self.get("/booking")

    def get_booking(self, booking_id):
        return self.get(f"/booking/{booking_id}")

    def create_booking(self, payload):
        return self.post("/booking", data=payload)
    
    def update_booking(self, booking_id, payload, token):
        return self.put(f"/booking/{booking_id}", data=payload, headers={"Cookie": f"token={token}"})

    def patch_booking(self, booking_id, payload, token):
        return self.patch(f"/booking/{booking_id}", data=payload, headers={"Cookie": f"token={token}"})
    
    def delete_booking(self, booking_id, token):
        return self.patch(f"/booking/{booking_id}", headers={"Cookie": f"token={token}"})