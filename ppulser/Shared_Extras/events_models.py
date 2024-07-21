from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash


db = SQLAlchemy()

       

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    event_date = db.Column(db.DateTime, nullable=False)
    venue = db.Column(db.String, nullable=False)
    start_time = db.Column(db.Dateime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    event_type = db.Column(db.String, nullable=False)
    music_type = db.Column(db.String, nullable=False)
    organizer = db.Column(db.String, nullable=False)
    entry_fees = db.Column(db.String, nullable=False)
    

    def __init__(self, event_name, description, event_date, venue, start_time, end_time, event_type, music_type, organizer, entry_fees ):
        self.event_name = event_name
        self.desciption = description
        self.event_date = event_date
        self.venue = venue
        self.start_time = start_time
        self.end_time = end_time
        self.event_type = event_type
        self.music_type = music_type
        self.organizer = organizer
        self.entry_fees = entry_fees
     
    def save(self):
        db.session.add(self)
        db.session.commit()
     
 