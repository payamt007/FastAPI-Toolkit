import os

from sqlmodel.ext.asyncio.session import AsyncSession

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from sqlmodel import SQLModel, create_engine

db_driver = os.environ.get("DB_DRIVER")
user = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")
db = os.environ.get("POSTGRES_DB")
db_host = os.environ.get("POSTGRES_HOST")

DATABASE_URL = f"{db_driver}{user}:{password}@{db_host}:5432/{db}"
# DATABASE_URL = "sqlite+aiosqlite:///database.db"

engine = create_async_engine(DATABASE_URL, echo=True, future=True)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
