import uuid
from datetime import datetime

from sqlalchemy import String, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.db.database import Base


class Payments(Base):
    __tablename__ = "payments"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    booking_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("bookings.id"))
    payment_time: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )

    booking: Mapped["Booking"] = relationship(back_populates="payment")
