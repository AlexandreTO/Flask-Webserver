from flask import render_template, jsonify, redirect, url_for, Blueprint

# Blueprints
routes = Blueprint('routes', __name__)

@routes.route("/")
def index():
    return 'Index Page'

@routes.route("/hello")
def hello_world():
    return render_template('index.html')

@routes.route("/admin")
def hello_admin():
    return 'Admin'

@routes.route("/user/<name>")
def hello_user(name):
    return 'Hello %s' % name

### URL BUILDING
@routes.route('/user/<name>')
def hello_specific_name(name):
    if name == 'Alexandre':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_user', name = name ))

# JSON test
def json_response():
    response = {"name": "Alexandre", "age": 29}
    return jsonify([response])