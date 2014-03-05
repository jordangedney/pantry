from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = True)

class UserForm(Form):
    first = TextField('first', validators = [Required()])
    last = TextField('last', validators = [Required()])
    email = TextField('last', validators = [Required()])

if False: """
class RecipeForm(Form):
    # TODO: need to set time and  servings to appropriate fields
    name = TextField('first', validators = [Required()])
    ingredients = TextField('last', validators = [Required()])
    instructions = TextField('last', validators = [Required()])
    time = TextField('last', validators = [Required()])
    category = TextField('last', validators = [Required()])
    servings = TextField('last', validators = [Required()])
    author = TextField('last', validators = [Required()]) """