from src.infrastructure.models import Film
from src.infrastructure.repository.base_repository import BaseRepository


class FilmRepository(BaseRepository):
    model = Film
