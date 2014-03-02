from flask import Flask
import SQLAlchemy

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
connection = engine.connect()

from app import views, models

