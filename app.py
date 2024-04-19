from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/about.html')
def about():
    user = {'username': 'Sara'}
    return render_template('about.html', title='Home', user=user)


@app.route('/GymFinder.html')
def GymFinder():
    callApi
    return render_template ('GymFinder.html')  

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

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/signup.html')
def signup():
    return render_template('signup.html')

@app.route('/profile.html', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        name = request.form.get('name')
        return render_template('profile.html', name=name)
    return render_template('profile.html', name=None)
    