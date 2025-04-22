from flask import Flask
import routing

app = Flask(__name__, template_folder="./templates", static_folder="./static")

if __name__ == 'main':
    app.run()