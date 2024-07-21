from flask import Blueprint
from website.controllers.viewsController import home, start, landing_page

views_blueprint = Blueprint("views_bp", __name__)


views_blueprint.route('/', methods=['GET'])(home)
views_blueprint.route('/start', methods=['GET'])(start)
views_blueprint.route('/landing-page', methods=['GET'])(landing_page)