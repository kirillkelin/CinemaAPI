from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.application.film.film_service import FilmService
from src.config import settings
from src.infrastructure.repository.film_repository import FilmRepository
from src.presentation.film.router import router as film_router


# class Application:
#     def __init__(self, app: FastAPI):
#         self.app = app
#
#     @classmethod
#     def create_app(cls):
#         app = FastAPI()
#
#         app.add_middleware(
#             CORSMiddleware,
#             allow_origins=settings.origins,
#             allow_credentials=True,
#             allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
#             allow_headers=["*"],
#         )
#         film_repository = FilmRepository(Film())
#         film_service = FilmService(film_repository)
#         app.state.film_service = lambda: film_service
#
#         app.include_router(film_router)
#         return cls(app=app)
#
#     def start(self):
#         uvicorn.run(self.app, host="0.0.0.0", port=5000)
#
#
# if __name__ == "__main__":
#     application = Application.create_app()
#     application.start()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["*"],
)
film_repository = FilmRepository()
film_service = FilmService(film_repository)
app.state.film_service = lambda: film_service

# booking_repository =

app.include_router(film_router)
