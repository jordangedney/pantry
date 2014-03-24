from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, IntegerField
from wtforms.validators import Required

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = True)

class UserForm(Form):
    first = TextField('first', validators = [Required()])
    last = TextField('last', validators = [Required()])
    email = TextField('email', validators = [Required()])

class RecipeForm(Form):
    name = TextField('name', validators = [Required()])
    ingredients = TextField('ingredients', validators = [Required()])
    instructions = TextField('instructions', validators = [Required()])
    time = IntegerField('time', validators = [Required()])
    category = TextField('category', validators = [Required()])
    servings = IntegerField('servings', validators = [Required()])