from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def get_app():
    return Flask(__name__)

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)
db.init_app(app)
