import asyncio
import logging

from sqlalchemy import MetaData
from sqlmodel import Session, select
from tenacity import (after_log, before_log, retry, stop_after_attempt,
                      wait_fixed)

from app.db import engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1

meta = MetaData()


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
            # Try to create session to check if DB is awake
            await conn.execute(select(1))
    except Exception as e:
        print(e)
        logger.error(e)
        raise e


async def main() -> None:
    logger.info("Initializing service")
    await init()
    logger.info("Service finished initializing")


if __name__ == "__main__":
    asyncio.run(main())
