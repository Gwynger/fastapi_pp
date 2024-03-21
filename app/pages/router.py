from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/pages",
    tags=["Frontend"]
)

templates = Jinja2Templates(directory="app/templates")