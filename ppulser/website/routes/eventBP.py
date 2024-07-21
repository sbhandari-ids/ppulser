from flask import Blueprint
from website.controllers.eventController import view_event, upcoming_events, nearby_events, free_events, nightclub_events, popular_events, recommended_events, trending_events

event_blueprint = Blueprint("event_bp", __name__)


event_blueprint.route('/<id>', methods=['GET'])(view_event)
event_blueprint.route('/upcoming', methods=['GET'])(upcoming_events)
event_blueprint.route('/nearby', methods=['GET'])(nearby_events)
event_blueprint.route('/nightclubs', methods=['GET'])(nightclub_events)
event_blueprint.route('/free', methods=['GET'])(free_events)
event_blueprint.route('/popular', methods=['GET'])(popular_events)
event_blueprint.route('/recommended', methods=['GET'])(recommended_events)
event_blueprint.route('/trending', methods=['GET'])(trending_events)