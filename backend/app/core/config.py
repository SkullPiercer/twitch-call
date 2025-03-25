from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = "test"
    bot_token: str = "Your token here"
    webhook_url: str = "qwerty.kz"

    class Config:
        env_file = ".env"
        extra = "allow"


settings = Settings()
