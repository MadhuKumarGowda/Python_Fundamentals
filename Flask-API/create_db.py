from api import app, db

with app.app_context():
    # Below we create tables in database
    db.create_all()