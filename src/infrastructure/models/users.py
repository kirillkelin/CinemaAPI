import uuid
from datetime import date, datetime
from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.db.database import Base


class Users(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    first_name: Mapped[str] = mapped_column(String(64))
    last_name: Mapped[str] = mapped_column(String(64))
    middle_name: Mapped[Optional[str]] = mapped_column(String(64))
    birth_date: Mapped[date]
    email: Mapped[str] = mapped_column(String(64))
    hashed_password: Mapped[str]
    created_at: [datetime] = mapped_column(default=datetime.utcnow())
    updated_at: [datetime] = mapped_column(
        default=datetime.utcnow(), onupdate=datetime.utcnow
    )
