from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class SeismicEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(128))
    magnitude = db.Column(db.Float)
    time = db.Column(db.DateTime)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
