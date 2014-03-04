from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy import create_engine

app = Flask(__name__)
app.config.from_object('config')
engine_url = sqlalchemy.engine.url.URL('mysql',
                                        username='pantry',
                                        password='pantrydb',
                                        host='localhost',
                                        port=3306,
                                        database='Pantry',
                                        query=None)

engine = create_engine(engine_url)
db = SQLAlchemy(app)
#db = SQLAlchemy(app, session_options={'engine':engine})
connection = engine.connect()

from app import views, models
