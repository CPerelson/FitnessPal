from flask import Blueprint, render_template, Flask, jsonify, request
from . import db
from flask_login import login_required, current_user
import googlemaps
import datetime

app = Blueprint('app', __name__)

gmaps = googlemaps.Client(key='AIzaSyCKHN7F6eHLoJBAAwAvHfRh20qFaRYtjwM')



@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/profile')
@app.route('/profile.html')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@app.route('/about.html')
def about():
    user = {'username': 'Sara'}
    return render_template('about.html', title='Home', user=user)

 
@app.route('/Calendar.html')
def Calendar():
    # Get the current date
    current_date = datetime.date.today().isoformat()
    return render_template('Calendar.html', current_date=current_date)

@app.route('/Statistics.html')
def Statistics():
    return render_template ('Statistics.html')

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