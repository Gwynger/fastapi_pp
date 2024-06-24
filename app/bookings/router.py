from datetime import date

from fastapi import APIRouter, BackgroundTasks, Depends
from pydantic import parse_obj_as
from fastapi_versioning import version

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBookingInfo, SNewBooking
from app.exceptions import RoomCannotBeBooked
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"],
)


@router.get("")
@version(1)
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBookingInfo]:
    return await BookingDAO.find_all(user_id=user.id)


@router.post("", status_code=201)
@version(2)
async def add_booking(
    booking: SNewBooking,
    background_tasks: BackgroundTasks,
    user: Users = Depends(get_current_user),
):
    booking = await BookingDAO.add(
        user.id,
        booking.room_id,
        booking.date_from,
        booking.date_to,
    )
    if not booking:
        raise RoomCannotBeBooked
    booking = parse_obj_as(SNewBooking, booking).dict()
    return booking


@router.delete("/{booking_id}")
@version(1)
async def remove_booking(
    booking_id: int,
    current_user: Users = Depends(get_current_user),
):
    await BookingDAO.delete(id=booking_id, user_id=current_user.id)