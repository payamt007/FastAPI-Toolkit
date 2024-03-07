import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from .db import get_db_session
from .main import app


@pytest_asyncio.fixture(name="session")
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


@pytest_asyncio.fixture(name="client")
async def client_fixture(session: AsyncSession):
    def get_session_override():
        return session

    app.dependency_overrides[get_db_session] = get_session_override

    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as async_client:
        yield async_client

    app.dependency_overrides.clear()
