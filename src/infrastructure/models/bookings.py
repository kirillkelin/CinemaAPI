import uuid
from datetime import datetime
from enum import Enum

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.db.database import Base


class PaymentStatusEnum(Enum):
    PAID = "paid"
    NOT_PAID = "not paid"


class Bookings(Base):
    __tablename__ = "bookings"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    film_session_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("film_sessions.id"))
    payment_status: Mapped[PaymentStatusEnum] = mapped_column(name="payment_status")
    row: Mapped[int]
    seat: Mapped[int]
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )
    price: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.utcnow,
    )

    user: Mapped["Users"] = relationship(back_populates="bookings")
    payment: Mapped["Payments"] = relationship(back_populates="booking")
    film_session: Mapped["FilmSessions"] = relationship(back_populates="booking")
