from celery.utils.log import get_task_logger
from sqlmodel import Session, select

from ..celery import celery_app
from ..db import engine
from ..songs.models import Song

logger = get_task_logger(__name__)


@celery_app.task
def sample_task() -> None:
    logger.info("Doing some sample task 😄")
    with Session(engine) as session:
        songs = session.exec(select(Song)).all()
        [
            logger.info(
                f"Song Record : {song.name},{song.artist},{song.year},{song.id},{song.description}"
            )
            for song in songs
        ]
