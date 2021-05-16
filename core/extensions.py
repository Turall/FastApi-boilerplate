from core.factories import settings
from ssl import create_default_context
from gino.ext.starlette import Gino


if not settings.DEBUG:
    ssl_object = create_default_context(cafile=settings.SSL_CERT_FILE)

    db: Gino = Gino(
        dsn=settings.DATABASE_URL,
        echo=False,
        ssl=ssl_object,
        pool_min_size=3,
        pool_max_size=20,
        retry_limit=1,
        retry_interval=1,
    )
else:

    db: Gino = Gino(
        dsn=settings.DATABASE_URL)
