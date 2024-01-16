from fastapi import Request

from src.application.film.film_service import FilmService


def film_service_scope(request: Request) -> FilmService:
    return request.app.state.film_service()
