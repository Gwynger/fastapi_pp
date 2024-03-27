from celery import Celery

celery = Celery(
    "tasks",
    brocker="redis://localhost:6379",
    include=["app.tasks.tasks"]
)

