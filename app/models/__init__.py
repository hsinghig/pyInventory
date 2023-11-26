from sqlalchemy import PrimaryKeyConstraint
from ..extensions import db


class tblwidth(db.Model):
    __table_args__ = {"schema":"ip"}
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    isActive = db.Column(db.Boolean())
    comment = db.Column(db.String())