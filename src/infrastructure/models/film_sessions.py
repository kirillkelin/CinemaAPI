import uuid
from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.db.database import Base


class FilmSessions(Base):
    __tablename__ = "film_sessions"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    film_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("movie_session.id"))
    cinema_hall_id: Mapped[int] = mapped_column(ForeignKey("cinema_halls.id"))
    start_time: Mapped[datetime] = mapped_column(
        default=datetime.utcnow().strftime("%Y-%m-%dT%H:%M")
    )
