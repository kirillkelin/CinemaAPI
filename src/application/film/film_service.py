import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src.application.schemas.film_schema import FilmResponse, Film


class FilmService:
    def __init__(self, repository):
        self.repository = repository

    async def get_all_films(self, session: AsyncSession):
        result = await self.repository.get_all(session=session)
        return [FilmResponse.model_validate(film) for film in result]

    async def get_film_by_id(self, session: AsyncSession, film_id: uuid.UUID):
        film = await self.repository.find_one_or_none(session=session, id=film_id)
        return FilmResponse.model_validate(film)

    async def add_film(self, session: AsyncSession, film: Film):
        result = await self.repository.add(
            session=session,
            title=film.title,
            director=film.director,
            description=film.description,
            release_date=film.release_date,
            duration=film.duration,
            is_in_cinemas=film.is_in_cinemas,
        )
