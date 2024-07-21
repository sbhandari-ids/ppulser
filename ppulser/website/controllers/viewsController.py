from flask import request, render_template, jsonify, flash, redirect, url_for
from website.services.events_services import get_events
from flask_login import login_required, current_user


@login_required
def home():
    events = get_events()
    return render_template('home.html', user = current_user, events = events)

def start():
    return render_template('start.html')

def landing_page():
    return render_template('landingPage.html')