from flask import request, render_template, jsonify, flash, redirect, url_for
from website.services.events_services import get_event_by_id, get_free_events, get_popular_events, get_recommended_events, get_trending_events



def view_event(id):
    event = get_event_by_id(id)
    print(event)
    string = '<h1>' + event.event_name + '</h1>'
    return render_template('event_details.html', event=event)

def upcoming_events():
    return '<h1>Upcoming events</h1>'

def nearby_events():
    return render_template('nearbyEvents.html')

def nightclub_events():
    return '<h1>Nightclubs</h1>'

def free_events():
    events = get_free_events()
    return render_template('event_free.html', events=events)

def popular_events():
    pop_events = get_popular_events()
    return render_template('event_popular.html', events=pop_events)

def recommended_events():
    rec_events = get_recommended_events()
    return render_template('event_recommended.html', events=rec_events)

def trending_events():
    trend_events = get_trending_events()
    return render_template('event_trending.html', events=trend_events)