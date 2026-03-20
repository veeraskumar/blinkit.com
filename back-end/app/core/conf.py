from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str
    max_size: int = 5 * 1024 * 1024
    username: str
    password: str
    algorithm: str = "HS256"
    secret_key: str
    access_token_expire_hours: int = 1
    cloud_name: str
    api_key: str
    api_secret: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()  # type: ignore
