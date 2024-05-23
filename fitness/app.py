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
        zipcode = request.form.get('zipcode')
        location = get_location_coordinates(zipcode)
        if location:
            recommended_gyms = recommend_gyms(location)
            return jsonify(recommended_gyms)
        else:
            return jsonify([])
    elif request.method == 'GET' and 'zipcode' in request.args:
        zipcode = request.args.get('zipcode')
        location = get_location_coordinates(zipcode)
        if location:
            recommended_gyms = recommend_gyms(location)
            return jsonify(recommended_gyms)
        else:
            return jsonify([])
    return render_template('GymFinder.html', zipcode='')

def get_location_coordinates(zipcode):
    geocode_result = gmaps.geocode(address=zipcode)
    if geocode_result:
        location = geocode_result[0]['geometry']['location']
        return location['lat'], location['lng']
    else:
        return None

def recommend_gyms(location):
    places = gmaps.places_nearby(location=location, radius=5000, type='gym')
    nearby_gyms = [{'name': place['name'], 'vicinity': place.get('vicinity', 'N/A')} for place in places['results']]
    return nearby_gyms