from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    """Note database model"""
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10500))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # Update the date
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    """User database model"""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(50))
    first_name = db.Column(db.String(80))
    notes = db.relationship('Note') # add into user's note it's id 

