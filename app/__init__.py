import os
<<<<<<< HEAD
from flask.ext.login import LoginManager
=======
>>>>>>> 31b83d677390b3057c340d92931c8c8aa83e8215
from config import basedir
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy import create_engine

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

<<<<<<< HEAD
lm = LoginManager()
lm.init_app(app)
#oid = OpenID(app, os.path.join(basedir, 'app/db_repository/tmp'))

=======
>>>>>>> 31b83d677390b3057c340d92931c8c8aa83e8215
from app import views, models


