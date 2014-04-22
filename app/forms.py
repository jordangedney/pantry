from app import db, models
from flask.ext.wtf import Form
from flask.ext.wtf.file import FileField, FileAllowed, FileRequired
from wtforms import TextField, TextAreaField, BooleanField, IntegerField, SelectMultipleField
from wtforms.validators import Required
from operator import itemgetter

class LoginForm(Form):
    remember_me = BooleanField('remember_me', default = True)

class EditUserForm(Form):
    first_name = TextField('first', validators = [Required()])
    last_name = TextField('last', validators = [Required()])
    image = FileField('image', validators=[FileAllowed(('jpg',), '.JPG only!')])

class SearchForm(Form):
    search = TextField('search', validators = [Required()])
    
class RecipeForm(Form):
    name = TextField('name', validators = [Required()])
    instructions = TextAreaField('instructions', validators = [Required()])
    time = IntegerField('time', validators = [Required()])
    difficulty = IntegerField('difficulty', validators = [Required()])
    servings = IntegerField('', validators = [Required()])
    image = FileField('image', validators=[FileRequired(), FileAllowed(('jpg',), '.JPG only!')])

class IngredientForm(Form):
    name = TextField('name', validators = [Required()])
