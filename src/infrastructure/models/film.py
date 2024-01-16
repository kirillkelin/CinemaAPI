import uuid
from datetime import date
from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.db.base import Base


class Film(Base):
    __tablename__ = "film"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str]
    directors: Mapped[str]
    description: Mapped[Optional[str]] = mapped_column(String(2000))
    release_date: Mapped[date]
    duration: Mapped[int]
    in_cinemas: Mapped[bool] = mapped_column(default=True)

    film_sessions: Mapped[list["FilmSession"]] = relationship(back_populates="film")
