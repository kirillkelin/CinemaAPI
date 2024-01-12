import uuid
from datetime import datetime
from enum import Enum

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.db.base import Base


class PaymentStatusEnum(Enum):
    PAID = "paid"
    NOT_PAID = "not paid"


class Booking(Base):
    __tablename__ = "booking"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    film_session_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("film_session.id"))
    payment_status: Mapped[str]
    row: Mapped[int]
    seat: Mapped[int]
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE")
    )
    price: Mapped[float]
    created_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.utcnow,
    )

    user: Mapped["User"] = relationship(back_populates="bookings")
    payment: Mapped["Payment"] = relationship(back_populates="booking")
    film_session: Mapped["FilmSession"] = relationship(back_populates="booking")
