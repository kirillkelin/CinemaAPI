import uuid
from datetime import date
from typing import Optional

from pydantic import BaseModel


class Film(BaseModel):
    name: str
    directors: str
    description: Optional[str]
    release_date: date
    duration: int
    in_cinemas: bool = True

    class Config:
        from_attributes = True


class FilmResponse(Film):
    id: uuid.UUID

    class Config:
        from_attributes = True
