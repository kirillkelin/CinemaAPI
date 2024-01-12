from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.db.base import Base


class BranchOffice(Base):
    __tablename__ = "branch_office"

    id: Mapped[int] = mapped_column(primary_key=True)
    city: Mapped[str] = mapped_column(String(64))
    address: Mapped[str] = mapped_column(String(256))
    description: Mapped[str] = mapped_column(String(512))

    cinema_halls: Mapped[list["CinemaHall"]] = relationship(
        back_populates="branch_office"
    )
