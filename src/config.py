from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASS: str = "postgres"
    DB_NAME: str = "cinema_app"
    DB_ECHO: bool = False

    @property
    def get_database_url(self):
        user = f"{self.DB_USER}:{self.DB_PASS}"
        database = f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return f"postgresql+asyncpg://{user}@{database}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
