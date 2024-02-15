from app.celery import celery_app
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@celery_app.task
def sample_task() -> None:
    logger.info(f"Doing some sample task 😄")