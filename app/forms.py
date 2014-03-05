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