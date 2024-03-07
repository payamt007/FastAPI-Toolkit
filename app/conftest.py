import pytest
from httpx import AsyncClient
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from .db import Base, get_db_session
from .main import app


@pytest.fixture(name="session")
async def session_fixture():
    engine = create_async_engine(
        "sqlite+aiosqlite:///database.db", connect_args={"check_same_thread": False}
    )
    async_session = async_sessionmaker(engine, expire_on_commit=False)
    # meta = MetaData()
    # async with engine.begin() as conn:
    #     await conn.run_sync(Base.meta.create_all)
    session = async_session()
    try:
        yield session
    finally:
        await session.close()


@pytest.fixture(name="client")
async def client_fixture(session: AsyncSession):
    def get_session_override():
        return session

    app.dependency_overrides[get_db_session] = get_session_override

    async_client = AsyncClient(app=app, base_url="http://127.0.0.1:8000")
    try:
        yield async_client
    finally:
        await async_client.aclose()  # Close the AsyncClient after the test

    app.dependency_overrides.clear()
