from __future__ import annotations

import os

from sqlmodel import create_engine

# DATABASE_URL = "sqlite+aiosqlite:///database.db"
DATABASE_URL = os.environ.get("DATABASE_URL") or "sqlite:///database.db"

# engine = create_async_engine(DATABASE_URL, echo=True, future=True)
engine = create_engine(DATABASE_URL, echo=True)

# engine = create_engine("sqlite:///database.db", echo=True)

# async def init_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(SQLModel.metadata.drop_all)
#         await conn.run_sync(SQLModel.metadata.create_all)

# async def get_session() -> AsyncSession:
#     async_session = sessionmaker(
#         engine, class_=AsyncSession, expire_on_commit=False
#     )
#     async with async_session() as session:
#         yield session
