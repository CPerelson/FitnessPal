from flask import render_template, Flask, jsonify, redirect, request, Blueprint
import googlemaps
import datetime 
#from forms import LoginForm, RegistrationForm
#from app import db
from .models import User
from flask_login import login_required, current_user, login_user, logout_user
import sqlalchemy as sa
from flask import flash, redirect, url_for
from . import db
from .forms import LoginForm, RegistrationForm

app = Blueprint('app', __name__)

#Initialize Flask app
app = Flask(__name__)

#Initialize googlemaps
gmaps = googlemaps.Client(key='AIzaSyCKHN7F6eHLoJBAAwAvHfRh20qFaRYtjwM')

#Routes
#@app.route('/')
@app.route('/loginPage.html', methods=['GET', 'POST'])
@login_required
def user_login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))    
    
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data)).scalar()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return render_template('loginPage.html', title='Sign In', form=form)
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            return redirect(url_for('index.html'))
    return render_template('loginPage.html', title='Sign In', form=form)

@app.route('/')
@app.route('/index.html')
#@login_required
def index():
    # TODO: read notes from DB
    notes=[{"text": "note1", "date": "20240201", "text": "note2"}, {"text": "note2", "date": "20240301"}]
    return render_template('index.html', title='Home', notes=notes, current_user=current_user)

@app.route('/about.html')
def about():
    user = {'username': 'Sara'}
    return render_template('about.html', title='Home', user=user)

#@app.route('/Calender.html')
#def Calender():
    #return render_template ('Calender.html')  
@app.route('/Calender.html')
def Calender():
    # Get the current date
    current_date = datetime.date.today().isoformat()
    return render_template('Calender.html', current_date=current_date)

@app.route('/Statistics.html')
def Statistics():
    return render_template ('Statistics.html')  

@app.route('/Main.html')
def Main():
    return render_template ('Main.html')

@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('loginPage'))
    return render_template('signup')

@app.route('/profile.html')
@login_required
def profile():
    return render_template('profile')


@app.route('/GymFinder.html', methods=['GET', 'POST'])
def GymFinder():
    if request.method == 'POST':
        # Retrieve user's location (zipcode) from the form data
        zipcode = request.form.get('zipcode')
        
        # Get the latitude and longitude coordinates for the provided zipcode
        location = get_location_coordinates(zipcode)
        
        if location:
            # Call a function to recommend gyms based on the user's location
            recommended_gyms = recommend_gyms(location)
            
            # Return recommended gyms as JSON response
            return jsonify(recommended_gyms)
        else:
            return jsonify([])
    
    # Render the GymFinder.html template with an empty form
    return render_template('GymFinder.html', zipcode='')

def get_location_coordinates(zipcode):
    # Geocode the zipcode to retrieve latitude and longitude coordinates
    geocode_result = gmaps.geocode(address=zipcode)
    
    if geocode_result:
        location = geocode_result[0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        return latitude, longitude
    else:
        return None

def recommend_gyms(location):
    # Perform a nearby search for gyms based on the provided location
    places = gmaps.places_nearby(location=location, radius=5000, type='gym')
    
    # Extract relevant information about each gym
    nearby_gyms = [{'name': place['name'], 'vicinity': place.get('vicinity', 'N/A')} for place in places['results']]
    
    # Return the list of recommended gyms
    return nearby_gyms

@app.route('/logout')
@login_required
def logout():
    logout_user()
    request.args
    return redirect(url_for('loginPage.html'), code=302)


