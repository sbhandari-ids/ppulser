from website.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask import flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from website.database import db

def create_user(email, password, username):
    new_user = User(email=email, password=generate_password_hash(password), username=username)
    db.session.add(new_user)
    db.session.commit()
    login_user(new_user, remember=True)
    flash('You have been logged in!', category='success')
    return new_user

def loginU(email, password):
    user = User.query.filter_by(email=email).first()
    if user:
        if check_password_hash(user.password, password):
            login_user(user, remember=True)
            flash('Logged in successfully', category='success')
            return True
        else:
            flash('Wrong password, try again.', category='error')
            return False
    else:
        flash('That email does not have an account!', category='error')
        return False
    
