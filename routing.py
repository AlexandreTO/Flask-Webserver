from flask import render_template, jsonify
from hello_world import app

@app.route("/")
def index():
    return 'Index Page'

@app.route("/hello")
def hello_world():
    return render_template('index.html')

@app.route('/hello/<user>')
def hello_user(user):
    return 'Hello %s' % user

@app.route("/")
def index():
    return 'Index Page'

# JSON test
def json_response():
    response = {"name": "Alexandre", "age": 29}
    return jsonify([response])