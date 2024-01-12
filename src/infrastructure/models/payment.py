import uuid
from datetime import datetime

from sqlalchemy import String, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.db.base import Base


class Payment(Base):
    __tablename__ = "payment"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    booking_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("booking.id"))
    payment_time: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )

    booking: Mapped["Booking"] = relationship(back_populates="payment")
