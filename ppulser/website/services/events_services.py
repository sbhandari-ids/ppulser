from website.models.event import Event
from flask import flash, redirect, url_for
from website.database import db

def get_events():
    events = []
    for i in range(1,7):
        events.append(Event.query.filter_by(id=i).first())
    return events

def get_event_by_id(id):
    event = Event.query.filter_by(id=id).first()
    print(event)
    return event

def get_free_events():
    free_events = Event.query.filter_by(entry_fees='0').all()
    return free_events

def get_popular_events():
    pop_events = Event.query.filter_by(event_type='Popular').all()
    return pop_events

def get_recommended_events():
    rec_events = Event.query.filter_by(event_type='Recommended').all()
    return rec_events

def get_trending_events():
    trend_events = Event.query.filter_by(event_type='Trending').all()
    return trend_events