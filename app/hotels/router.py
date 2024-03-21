from datetime import date, datetime
from typing import List
from fastapi import APIRouter, Query
from app.hotels.dao import HotelDAO
from app.hotels.schemas import SHotel, SHotelInfo

router = APIRouter(
    prefix="/hotels",
    tags=["Hotels"]
)

@router.get("")
async def get_hotels_by_location_and_time(
    location: str,
    date_from: date = Query(..., description=f"Например, {datetime.now().date()}"),
    date_to: date = Query(..., description=f"Например, {datetime.now().date()}"), 
) -> List[SHotelInfo]:
    hotels = await HotelDAO.search_for_hotels(location, date_from, date_to)
    return hotels


@router.get("/{hotel_id}/rooms")
async def get_rooms_by_time(
    hotel_id: int,
    date_from: date = Query(..., description=f"Например, {datetime.now().date()}"),
    date_to: date = Query(..., description=f"Например, {datetime.now().date()}"), 
) -> List[SHotel]:
    rooms = await HotelDAO.search_for_rooms(hotel_id, date_from, date_to)
    return rooms