from fastapi import APIRouter
from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking

router = APIRouter(
    prefix='/bookings',
    tags=['Bookings'],
)

@router.get('')
async def get_bookings():  # -> list[SBooking] пока не работает
    return await BookingDAO.find_all()

