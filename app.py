from flask import Flask, render_template
from jinja2.ext import debug

app = Flask(__name__)

# list of dictionary...
JOBS = [
    {
        'id': 1,
        'title': 'Data Analysis',
        'location': 'Kandy',
        'salary': 'Rs. 10000'
    },
    {
        'id': 2,
        'title': 'Data Science',
        'location': 'Colombo',
        'salary': 'Rs. 12000'
    },
    {
        'id': 3,
        'title': 'Full Stack Developer',
        'location': 'Colombo',
        'salary': 'Rs. 8000'
    },
    {
        'id': 4,
        'title': 'Front-end Developer',
        'location': 'Gale',
    },
    {
        'id': 5,
        'title': 'Back-end Developer',
        'location': 'Colombo',
        'salary': 'Rs. 5000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)