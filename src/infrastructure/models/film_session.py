import uuid
from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.db.base import Base


class FilmSession(Base):
    __tablename__ = "film_session"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    film_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("film.id", ondelete="CASCADE")
    )
    cinema_hall_id: Mapped[int] = mapped_column(ForeignKey("cinema_hall.id"))
    start_time: Mapped[datetime] = mapped_column(
        default=datetime.utcnow().strftime("%Y-%m-%dT%H:%M")
    )

    booking: Mapped["Booking"] = relationship(back_populates="film_session")
    film: Mapped["Film"] = relationship(back_populates="film_sessions")
    cinema_hall: Mapped["CinemaHall"] = relationship(back_populates="film_sessions")
