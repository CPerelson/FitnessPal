from flask import render_template
from flask import Flask
import datetime 
from map import map_app

app = Flask(__name__)

<<<<<<< HEAD
app.register_blueprint(map_app)


=======
>>>>>>> c5acac7d0f12aaf5e3e0c76675f6aecc96bc9f97
@app.route('/about.html')
def about():
    user = {'username': 'Sara'}
    return render_template('about.html', title='Home', user=user)


#@app.route('/GymFinder.html')
#def GymFinder():
  #  callApi
    #return render_template ('GymFinder.html')  

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

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/signup.html')
def signup():
    return render_template('signup.html')

@app.route('/profile.html')
def profile():
    return render_template('profile.html')

@app.route('/')
@app.route('/loginPage.html')
def loginPage():
    return render_template('loginPage.html')

