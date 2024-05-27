import pytest
from app.config import settings
from app.database import Base, async_session_maker, engine
import json

from app.bookings.models import Bookings
from app.bookings.models import Hotels, Rooms
from app.bookings.models import Users


# Database management tool
@pytest.fixture
async def prepare_database(autouse=True):
    assert settings.MODE == "TEST"
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock_json(model:str):
        with open(f"app/tests/mock_{model}.json", "r") as file:
            return json.load(file)


