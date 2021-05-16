# write you database models in this file

from core.dbsetup import db, Model


class Example(Model):

    __tablename__ = "example"

    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, index=True)
