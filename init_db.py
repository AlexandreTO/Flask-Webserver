from book import app, db

with app.app.context():
    db.create_all()