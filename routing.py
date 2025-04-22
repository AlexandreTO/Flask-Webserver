from flask import render_template, jsonify, redirect, url_for
from hello_world import app

@app.route("/")
def index():
    return 'Index Page'

@app.route("/hello")
def hello_world():
    return render_template('index.html')

@app.route("/admin")
def hello_admin():
    return 'Admin'

@app.route("/user/<name>")
def hello_user(name):
    return 'Hello %s' % name

### URL BUILDING
@app.route('/user/<name>')
def hello_specific_name(name):
    if name == 'Alexandre':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_user', name = name ))

# JSON test
def json_response():
    response = {"name": "Alexandre", "age": 29}
    return jsonify([response])