from website.database import db


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(360), nullable=False)
    event_date = db.Column(db.String(100), nullable=False)
    venue = db.Column(db.String(100), nullable=False)
    start_time = db.Column(db.String(100), nullable=False)
    end_time = db.Column(db.String(100), nullable=False)
    event_type = db.Column(db.String(100), nullable=False)
    music_type = db.Column(db.String(100), nullable=False)
    organizer = db.Column(db.String(100), nullable=False)
    entry_fees = db.Column(db.String(100), nullable=False)
    
