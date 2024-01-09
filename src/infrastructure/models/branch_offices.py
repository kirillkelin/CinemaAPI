from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.db.database import Base


class BranchOffices(Base):
    __tablename__ = "branch_offices"

    id: Mapped[int] = mapped_column(primary_key=True)
    city: Mapped[str] = mapped_column(String(64))
    address: Mapped[str] = mapped_column(String(256))
    description: Mapped[str] = mapped_column(String(512))
