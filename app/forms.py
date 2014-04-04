from app import db, models
from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, IntegerField, SelectMultipleField
from wtforms.validators import Required
from operator import itemgetter

class LoginForm(Form):
    remember_me = BooleanField('remember_me', default = True)

class EditUserForm(Form):
    first_name = TextField('first', validators = [Required()])
    last_name = TextField('last', validators = [Required()])

class SearchForm(Form):
    search = TextField('search', validators = [Required()])
    
class RecipeForm(Form):
    name = TextField('name', validators = [Required()])
    ingredients = TextField('ingredients', validators = [Required()])
    instructions = TextField('instructions', validators = [Required()])
    time = IntegerField('time', validators = [Required()])
    category = TextField('category', validators = [Required()])
    servings = IntegerField('', validators = [Required()])

class IngredientForm(Form):
    name = TextField('name', validators = [Required()])

class IngredientSelector(Form):
    ingredients = models.Ingredient.query.all()
    choices = []
    for each in ingredients:
        tup = (str(each.id), each.name)
        choices.append(tup)

    # Sort the list alphabetically
    choices = sorted(choices, key=itemgetter(1))

    ingredient = SelectMultipleField(u'Programming Language', choices = choices)