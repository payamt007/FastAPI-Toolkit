import os

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

# declarative base class
Base = declarative_base()
# DATABASE_URL = "sqlite+aiosqlite:///database.db"
DATABASE_URL = os.environ.get("DATABASE_URL") or "sqlite+aiosqlite:///database.db"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)


# def get_session():
#     with Session(engine) as session:
#         yield session


# def get_session():
#     db = async_session()
#     try:
#         yield db
#     finally:
#         db.close()


async def get_db_session():
    db = async_session()
    try:
        yield db
    finally:
        await db.close()
