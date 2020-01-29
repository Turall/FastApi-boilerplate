# from sqlalchemy.ext.declarative import declarative_base
# # from core.factories import Session
from sqlalchemy import MetaData
from gino.ext.starlette import Gino
from core.factories import settings


db: MetaData = Gino(dsn=settings.DATABASE_URL)
