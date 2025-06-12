import os
from datetime import timedelta

from celery import Celery

celery_app = Celery(
    __name__,
    broker=os.environ.get("REDIS_URL") or "redis://localhost:6379",
    backend=os.environ.get("REDIS_URL") or "redis://localhost:6379",
    include=["app.tasks.tasks"],
)
celery_app.autodiscover_tasks()


@celery_app.task(bind=True)
def debug_task(self) -> None:
    print(f"Request: {self.request!r}")


celery_app.conf.beat_schedule = {
    "scrap_task": {
        "task": "app.tasks.tasks.sample_task",
        "schedule": timedelta(seconds=5),
    },
}
