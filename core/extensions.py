from gino.ext.starlette import Gino
from core.factories import settings




db: Gino = Gino(dsn=settings.DATABASE_URL)
