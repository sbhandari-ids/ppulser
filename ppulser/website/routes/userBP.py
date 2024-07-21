from flask import Blueprint
from website.controllers.userController import signup_email, login, logout, signup_password, sign_up_name

user_blueprint = Blueprint("user_bp", __name__)

user_blueprint.route('/signup-name', methods=['POST','GET'])(sign_up_name)
user_blueprint.route('/signup-email', methods=['POST','GET'])(signup_email)
user_blueprint.route('/signup-password', methods=['POST','GET'])(signup_password)
user_blueprint.route('/login', methods=['GET', 'POST'])(login)
user_blueprint.route('/logout', methods=['GET'])(logout)



# @app.route('/upload_profile_pic', methods=['POST']) 
