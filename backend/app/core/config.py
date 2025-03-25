from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = "test"
    bot_token: str = "Your token here"

    class Config:
        env_file = ".env"
        extra = "allow"


settings = Settings()
