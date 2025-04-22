from flask import Flask
from routing import routes

app = Flask(__name__, template_folder="./templates", static_folder="./static")
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run()   