from enum import Enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.db.base import Base


class CinemaHallTypeEnum(Enum):
    STANDARD = "standard"
    VIP = "vip"
    CINEMA_3D = "3D"


class CinemaHall(Base):
    __tablename__ = "cinema_hall"

    id: Mapped[int] = mapped_column(primary_key=True)
    cinema_hall_type: Mapped[str]
    rows_count: Mapped[int]
    seats_per_row: Mapped[int]
    branch_office_id: Mapped[int] = mapped_column(ForeignKey("branch_office.id"))

    film_sessions: Mapped[list["FilmSession"]] = relationship(
        back_populates="cinema_hall"
    )
    branch_office: Mapped["BranchOffice"] = relationship(back_populates="cinema_halls")
