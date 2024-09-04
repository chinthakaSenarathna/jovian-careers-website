from flask import Flask
from jinja2.ext import debug

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello jovian"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)