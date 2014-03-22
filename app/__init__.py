import os

from config import basedir
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy import create_engine

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models


