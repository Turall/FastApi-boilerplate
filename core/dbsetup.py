from uuid import uuid4
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType, Timestamp
from core.extensions import db     
relationship = relationship
Column,Integer,String,BOOLEAN,ForeignKey,Datetime = db.Column,db.Integer,db.String,db.BOOLEAN,db.ForeignKey,db.DateTime



class SurrogatePK(object):
    """A mixin that adds a surrogate UUID 'primary key' column named ``id`` to
    any declarative-mapped class."""

    __table_args__ = {"extend_existing": True}

    id = Column(UUIDType(binary=False), primary_key=True)


class Model(SurrogatePK,db.Model):
    __abstract__ = True

    @classmethod
    async def create(cls, **kwargs):
        if issubclass(cls, SurrogatePK):
            unique_id = uuid4()
            if not kwargs.get("id"):
                kwargs["id"] = unique_id
        return await cls(**kwargs)._create()

