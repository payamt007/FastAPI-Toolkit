import logging
import os

from sqlalchemy import MetaData, create_engine
from sqlmodel import Session, SQLModel, select
from tenacity import (
    after_log,
    before_log,
    retry,
    stop_after_attempt,
    wait_fixed,
)

DATABASE_URL = os.environ.get("DATABASE_URL") or "sqlite:///database.db"
engine = create_engine(DATABASE_URL, echo=True)

# from app.db import engine

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
def init() -> None:
    try:
        with Session(engine) as session:
            SQLModel.metadata.create_all(engine)
            session.exec(select(1))
    except Exception as e:
        print(e)
        logger.error(e)
        raise e


def main() -> None:
    logger.info("Initializing service")
    init()
    logger.info("Service finished initializing")


if __name__ == "__main__":
    main()
# asyncio.run(main())
