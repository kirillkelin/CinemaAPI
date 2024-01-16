from src.infrastructure.models import Film
from src.infrastructure.repository.base_repository import BaseRepository


class FilmRepository(BaseRepository):
    # def __init__(self, model):
    #     super().__init__(model)

    model = Film
