CREATE_BOOKING = {
    "firstname": "Neeraj",
    "lastname": "Joshi",
    "totalprice": 500,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2026-07-10",
        "checkout": "2026-07-15"
    },
    "additionalneeds": "Breakfast"
}


UPDATE_BOOKING = {
    "firstname": "Sita",
    "lastname": "Ram",
    "totalprice": 700,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2026-07-10",
        "checkout": "2026-07-15"
    },
    "additionalneeds": "Lunch"
}

PATCH_BOOKING = {
    "firstname": "Neeraj"
    }


INVALID_BOOKING = {
    "firstname": 123,
    "lastname": True
}