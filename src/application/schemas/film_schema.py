import uuid
from datetime import date
from typing import Optional

from pydantic import BaseModel


class Film(BaseModel):
    title: str
    director: str
    description: Optional[str]
    release_date: date
    duration: int
    is_in_cinemas: bool = True

    class Config:
        from_attributes = True


class FilmResponse(Film):
    id: uuid.UUID

    class Config:
        from_attributes = True
