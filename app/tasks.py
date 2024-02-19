from __future__ import annotations

from celery.utils.log import get_task_logger

from .celery import celery_app

logger = get_task_logger(__name__)


@celery_app.task
def sample_task() -> None:
    logger.info("Doing some sample task 😄")
