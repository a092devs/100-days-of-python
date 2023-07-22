import requests
import random
from datetime import date
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    current_year = date.today().year
    random_num = random.randint(1, 10)
    return render_template('index.html', num = random_num, year=current_year)

@app.route('/guess/<name>')
def guess(name):
    name = name.title()
    age = requests.get(f'https://api.agify.io?name={name}').json()
    gender = requests.get(f'https://api.genderize.io?name={name}').json()
    data = {
        'age' : age['age'],
        'gender' : gender['gender'],
        'name' : name
    }
    return render_template('guess.html', **data)

if __name__ == '__main__':
    app.run(debug=True)