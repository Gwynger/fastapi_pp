from app.tasks.celery import celery
from PIL import Image
from pathlib import Path



@celery.task
def process_pic(
    path: str,
):
    img_path = Path(path)
    img = Image.open(img_path)
    img_resized_max = img.resize((1000, 500))
    img_resized_min = img.resize((200, 100))
    img_resized_max.save(f"app/static/images/resiized_max{img_path.name}")
    img_resized_min.save(f"app/static/images/resiized_min{img_path.name}")