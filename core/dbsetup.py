from uuid import uuid4
from sqlalchemy_utils import UUIDType, Timestamp # add created,updated columns to model
from core.extensions import db


class SurrogatePK(object):
    """A mixin that adds a surrogate UUID 'primary key' column named ``id`` to
    any declarative-mapped class."""

    __table_args__ = {"extend_existing": True}

    id = db.Column(UUIDType(binary=False), primary_key=True)


class Model(Timestamp,SurrogatePK,db.Model):
    __abstract__ = True

    @classmethod
    async def create(cls, **kwargs):
        if issubclass(cls, SurrogatePK):
            unique_id = uuid4()
            if not kwargs.get("id"):
                kwargs["id"] = unique_id
        return await cls(**kwargs)._create()

