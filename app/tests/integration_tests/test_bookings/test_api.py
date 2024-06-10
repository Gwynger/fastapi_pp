import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "room_id, date_from, date_to, status_code, booked_rooms", [
        (4, "2030-01-01", "2030-01-29", 200, 3),
        (4, "2030-01-01", "2030-01-29", 200, 4),
        (4, "2030-01-01", "2030-01-29", 200, 5),
        (4, "2030-01-01", "2030-01-29", 200, 6),
        (4, "2030-01-01", "2030-01-29", 200, 7),
        (4, "2030-01-01", "2030-01-29", 200, 8),
        (4, "2030-01-01", "2030-01-29", 200, 9),
        (4, "2030-01-01", "2030-01-29", 200, 10),
        (4, "2030-01-01", "2030-01-29", 409, 10),
        (4, "2030-01-01", "2030-01-29", 409, 10),
    ]
)
async def test_add_and_get_booking(room_id, date_from, date_to, status_code, booked_rooms, 
                                   authenticated_ac: AsyncClient):
    response = await authenticated_ac.post("/bookings", params={
        "room_id": room_id,
        "date_from": date_from,
        "date_to": date_to,
    })

    assert response.status_code == status_code

    response = await authenticated_ac("/bookings")

    assert len(response.json()) == booked_rooms