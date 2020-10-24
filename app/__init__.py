import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


ROOT_FOLDER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


app = Flask(
    __name__,
    static_url_path="/assets",
    # static_folder=os.path.join(ROOT_FOLDER, "client", "dist", "assets"),
)

app.config.from_pyfile(os.path.join(ROOT_FOLDER, "config", "flask-dev.cfg"))

db = SQLAlchemy(app)

from . import views
