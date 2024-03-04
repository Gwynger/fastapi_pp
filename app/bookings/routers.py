from fastapi import APIRouter

router = APIRouter(
    prefix='/bookings',
    tags=['Bookings'],
)

@router.get('')
def get_bookings():
    pass

@router.get('/{booking_id}')
def get_bookings_next(booking_id):
    pass

