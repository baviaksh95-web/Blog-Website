#SQLAlchemy declaration section
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # Datetime is a class within SQLAlchemy, datetime is a module