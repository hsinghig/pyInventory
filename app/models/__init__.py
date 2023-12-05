from sqlalchemy import PrimaryKeyConstraint
from ..extensions import db


class tblwidth(db.Model):
    __table_args__ = {"schema":"ip"}
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    isActive = db.Column(db.Boolean())
    comment = db.Column(db.String())

class tblcolor(db.Model):
    __table_args__ = {"schema":"ip"}
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    isExtuder = db.Column(db.Boolean())
    isCrossPly = db.Column(db.Boolean())
    isActive = db.Column(db.Boolean())
    comment = db.Column(db.String())

class tbluser(db.Model):
    __table_args__ = {"schema":"ip"}
    id= db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(50))
    isActive = db.Column(db.Boolean())

class tblextruderlocation(db.Model):
    __table_args__ = {"schema":"ip"}
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))   
    isActive = db.Column(db.Boolean())

class tblextruder(db.Model):
    __table_args__ = {"schema":"ip"}
    id= db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer)
    color_id = db.Column(db.Integer)
    width_id = db.Column(db.Integer)
    length = db.Column(db.Integer)
    CreatedDate = db.Column(db.String)
    ModifiedDate = db.Column(db.String)
    CreatedBy_id = db.Column(db.Integer)
    ModifiedBy_id = db.Column(db.Integer)
    weight = db.Column(db.Float)

class tblextruderHist(db.Model):
    __table_args__ = {"schema":"ip"}
    id= db.Column(db.Integer, primary_key=True)
    extruder_id = db.Column(db.Integer)
    location_id = db.Column(db.Integer)
    color_id = db.Column(db.Integer)
    width_id = db.Column(db.Integer)
    length = db.Column(db.Integer)