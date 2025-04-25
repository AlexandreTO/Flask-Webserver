from book import app, db

# DB createfi
with app.app.context():
    db.create_all()