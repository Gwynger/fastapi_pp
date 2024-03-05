from sqlalchemy import select
from app.database import async_session_maker



class BaseDAO:
    
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.mappping().one_or_none()


    @classmethod
    async def find_one_or_none(cls, **kwargs):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**kwargs)
            result = await session.execute(query)
            return result.mappping().one_or_none()


    @classmethod     # упрощает синтаксис определяя принадлежность классу в целом
    async def find_all(cls, **kwargs):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**kwargs) # фильтры для запроса
            result = await session.execute(query)
            return result.mappings().all()