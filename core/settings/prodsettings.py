from starlette.config import Config
from starlette.datastructures import Secret
from core.settings.settings import BaseConfig


class ProdSettings(BaseConfig):

    """ Configuration class for site development environment """

    config = Config()

    DB_USER = config("DB_USER", cast=str)
    DB_PASSWORD = config("DB_PASSWORD", cast=Secret)
    DB_HOST = config("DB_HOST", cast=str)
    DB_PORT = config("DB_PORT", cast=str)
    DB_NAME = config("DB_NAME", cast=str)
    INCLUDE_SCHEMA = config("INCLUDE_SCHEMA", cast=bool)
    SSL_CERT_FILE = config("SSL_CERT_FILE")

    DATABASE_URL = config(
        "DATABASE_URL",
        default=f"asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    )
