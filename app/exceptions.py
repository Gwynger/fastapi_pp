from typing import Any, Dict

from fastapi import HTTPException, status
from typing_extensions import Annotated, Doc


class BookingException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(BookingException):
    status_code=status.HTTP_409_CONFLICT
    detail="The user already exists"


class IncorrectEmailOrPasswordException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Invalid e-mail or password"


class TokenExpiredException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "The token has expired"


class TokenEbsentException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "The token is missing"


class IncorrectTokenException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect token format"


class UserIsNotPresentException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED

class RoomCannotBeBooked(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "There are no rooms left"

class CannotAddDataToDatabase(BookingException):
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    detail="Failed to add a record"