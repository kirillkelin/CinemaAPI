import uuid
from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.db.database import Base


class Bookings(Base):
    __tablename__ = "bookings"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    movie_session_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("movie_session.id"))
    row: Mapped[int]
    seat: Mapped[int]
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    price: Mapped[int]
    created_at: [datetime] = mapped_column(default=datetime.utcnow())
