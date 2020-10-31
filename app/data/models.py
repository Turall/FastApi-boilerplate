# write you database models in this file

from core.dbsetup import (
    Column,
    Model,
    UUIDType,
    relationship,
    String,
    Integer,
    ForeignKey,
    BOOLEAN
)
from uuid import uuid4


#write your db models here

class Example(Model):
    """
    __tablename__ = "example"

    name = Column(String(),nullable=False)
    email = Column(String(),nullable=False,index=True)

    """
    pass
