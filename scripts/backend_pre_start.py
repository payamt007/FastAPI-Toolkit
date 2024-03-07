import asyncio
import logging
import os

from sqlalchemy import MetaData, select
from sqlalchemy.ext.asyncio import create_async_engine
from tenacity import (
    after_log,
    before_log,
    retry,
    stop_after_attempt,
    wait_fixed,
)

DATABASE_URL = os.environ.get("DATABASE_URL") or "sqlite+aiosqlite:///database.db"
engine = create_async_engine(DATABASE_URL, echo=True)
meta = MetaData()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
async def init() -> None:
    try:
        async with engine.begin() as conn:
            await conn.run_sync(meta.create_all)

            await conn.execute(select(1))
    except Exception as e:
        print(e)
        logger.error(e)
        raise e


async def main() -> None:
    logger.info("Initializing database service")
    await init()
    logger.info("Database Initialized successfully")


if __name__ == "__main__":
    asyncio.run(main())
