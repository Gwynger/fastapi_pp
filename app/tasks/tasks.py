from pydantic import EmailStr
from app.config import settings
from app.tasks.celery import celery
from PIL import Image
from pathlib import Path
import smtplib

from app.tasks.email_templates import create_booking_confirmation_template



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


@celery.task
def send_booking_confirmation_email(
    booking: dict,
    email_to: EmailStr,

):
    email_to_mock = settings.SMTP_USER
    msg_content = create_booking_confirmation_template(booking, email_to_mock)

    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg_content)