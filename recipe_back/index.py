from flask import Flask
import os

from models import db, Recipe

# Init app and database
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.abspath(os.getcwd())+"\\instance\\flaskr.sqlite"
db.init_app(app)
with app.app_context():
    db.create_all()


import routes

