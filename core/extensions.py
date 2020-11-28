
from sqlalchemy import MetaData
from gino.ext.starlette import Gino
from core.factories import settings




db: MetaData = Gino(dsn=settings.DATABASE_URL)
