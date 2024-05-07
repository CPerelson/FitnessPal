from flask import Blueprint, render_template
import requests

map_app = Blueprint('map_app', __name__, template_folder='templates')

def get_dist_dur(api_key, start, end):
   base_url = "https://maps.googleapis.com/maps/api/distancematrix/json"
   params = {
       "origins": start,
       "destinations": end,
       "key": api_key
   }

   response = requests.get(base_url, params=params)

   if response.status_code == 200:
       data = response.json()
       if data["status"] == "OK":
           distance = data["rows"][0]["elements"][0]["distance"]["text"]
           duration = data["rows"][0]["elements"][0]["duration"]["text"]
           return distance, duration
       else:
           print("Request failed.")
           print(data)
           return None, None
   else:
       print("Failed to make the request.")
       return None, None

@map_app.route('/GymFinder.html')
def GymFinder():
   api_key = "AIzaSyCKHN7F6eHLoJBAAwAvHfRh20qFaRYtjwM"  
   start = "681 crown street, brooklyn, new york, 11213"
   end = "1231 east 68th street, brookly, new york, 11234"
   distance, duration = get_dist_dur(api_key, start, end)
   return render_template('GymFinder.html', distance=distance, duration=duration)
