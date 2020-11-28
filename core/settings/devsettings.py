from starlette.config import Config
from starlette.datastructures import Secret,URL
from core.settings.settings import BaseConfig


class DevSettings(BaseConfig):

    """ Configuration class for site development environment """

    config = Config()

    DEBUG = config("DEBUG", cast=bool, default=True)
    
    DATABASE_URL = config(
        "DATABASE_URL",
        default="asyncpg:///db_name",
    )   