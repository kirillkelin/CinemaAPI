import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.film.film_service import FilmService
from src.application.schemas.film_schema import FilmResponse, Film
from src.infrastructure.db.database import database
from src.presentation.dependencies import film_service_scope

router = APIRouter(
    prefix="/films",
    tags=["Фильмы"],
)


@router.get("")
async def get_all_films(
    film_service: FilmService = Depends(film_service_scope),
    session: AsyncSession = Depends(database.get_session),
) -> list[FilmResponse]:
    return await film_service.get_all_films(session=session)


@router.get("/{id}")
async def get_film_by_id(
    film_id: uuid.UUID,
    film_service: FilmService = Depends(film_service_scope),
    session: AsyncSession = Depends(database.get_session),
) -> FilmResponse:
    return await film_service.get_film_by_id(session=session, film_id=film_id)


@router.post("")
async def add_film(
    film: Film,
    film_service: FilmService = Depends(film_service_scope),
    session: AsyncSession = Depends(database.get_session),
):
    pass
    # return await film_service.
