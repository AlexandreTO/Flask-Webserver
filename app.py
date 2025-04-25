from flask import Flask
from routing import routes
from flask_sqlalchemy import SQLAlchemy
from database import db

app = Flask(__name__, template_folder="./templates", static_folder="./static")

## Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(routes)

if __name__ == '__main__':
    app.run()   