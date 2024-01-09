from enum import Enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.db.database import Base


class CinemaHallTypeEnum(Enum):
    STANDARD = "standard"
    VIP = "vip"
    CINEMA_3D = "3D"


class CinemaHalls(Base):
    __tablename__ = "cinema_halls"

    id: Mapped[int] = mapped_column(primary_key=True)
    cinema_hall_type: Mapped[CinemaHallTypeEnum] = mapped_column(
        name="cinema_hall_type"
    )
    rows_count: Mapped[int]
    seats_per_row: Mapped[int]
    branch_office_id: Mapped[int] = mapped_column(ForeignKey("branch_offices.id"))
