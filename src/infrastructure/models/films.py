import uuid
from datetime import date
from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.db.database import Base


class Films(Base):
    __tablename__ = "films"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    directors: Mapped[list[str]] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(String(2000))
    release_date: Mapped[date]
    duration: Mapped[int]
    in_cinemas: Mapped[bool] = mapped_column(default=True)

    film_sessions: Mapped[list["FilmSessions"]] = relationship(back_populates="film")
