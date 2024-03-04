from sqlalchemy import select
from app.database import async_session_maker



class BaseDAO:
    
    model = None

    @classmethod     # упрощает синтаксис определяя принадлежность классу в целом
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.mappings().all()