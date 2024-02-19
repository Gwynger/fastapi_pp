from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DB_HOST = 'localhost'
DB_PORT = 5432
DB_USER = 'postgres'
DB_PASS = 'SD1582i'
DB_NAME = 'postgres'

DATABASE_URL = f'postresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'