from sqlalchemy import delete, select, insert
from app.database import async_session_maker



class BaseDAO:
    
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalars().one_or_none()


    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().one_or_none()


    @classmethod     # упрощает синтаксис определяя принадлежность классу в целом
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by) # фильтры для запроса
            result = await session.execute(query)
            return result.scalars().all()
        

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            result = await session.execute(query)
            await session.commit()
            return result.mappings().first()


    @classmethod
    async def delete(cls, **filter_by):
        async with async_session_maker() as session:
            query = delete(cls.model).filter_by(**filter_by)
            await session.execute(query)
            await session.commit()