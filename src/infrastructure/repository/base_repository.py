from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.db.base import Base
from src.infrastructure.models import Film


class BaseRepository:
    model = None

    @classmethod
    async def get_all(cls, session: AsyncSession):
        query = select(cls.model).select_from(cls.model)
        result = await session.execute(query)
        return result.scalars().all()

    @classmethod
    async def find_one_or_none(cls, session: AsyncSession, **filter_by):
        query = select(cls.model).select_from(cls.model).filter_by(**filter_by)
        result = await session.execute(query)
        return result.scalars().one_or_none()

    @classmethod
    async def add(cls, session: AsyncSession, **data):
        query = insert(cls.model).values(**data)
        await session.execute(query)
        await session.commit()
