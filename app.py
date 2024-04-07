from flask import render_template
from flask import Flask
from map import map_app

app = Flask(__name__)

app.register_blueprint(map_app)


@app.route('/about.html')
def about():
    user = {'username': 'Sara'}
    return render_template('about.html', title='Home', user=user)


#@app.route('/GymFinder.html')
#def GymFinder():
  #  callApi
    #return render_template ('GymFinder.html')  

@app.route('/Calender.html')
def Calender():
    return render_template ('Calender.html')  

@app.route('/Statistics.html')
def Statistics():
    return render_template ('Statistics.html')  

@app.route('/')
@app.route('/Main.html')
def Main():
    return render_template ('Main.html')