import asyncio

from celery.utils.log import get_task_logger
from sqlalchemy import update

from ..celery import celery_app
from ..db import async_session
from ..songs.models import Song

logger = get_task_logger(__name__)


async def get_songs():
    async with async_session() as session:
        await session.execute(
            update(Song).where(Song.id == 1).values(year=Song.year + 1)
        )
        await session.commit()


@celery_app.task
def sample_task() -> None:
    logger.info("Doing some sample task 😄")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_songs())
