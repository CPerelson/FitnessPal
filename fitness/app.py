from flask import Blueprint, render_template
from . import db
from flask_login import login_required, current_user

app = Blueprint('app', __name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)