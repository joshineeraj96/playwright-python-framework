from faker import Faker


fake = Faker()

def generate_booking_data():
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=100, max=1000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-07-15",
            "checkout": "2026-07-20"
        },
        "additionalneeds": "Breakfast"
    }
