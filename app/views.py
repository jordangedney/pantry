from app import app
import models
from flask import render_template, request, flash, redirect
from sqlalchemy import create_engine
from forms import LoginForm, UserForm



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user', methods = ['GET', 'POST'])
def new_user():
    form = UserForm()
    if form.validate_on_submit():
        flash('New user created!')
        return redirect('/index')
    return render_template('new_user.html', form = form)


@app.route('/get_users')
def get_recipe():
    users = models.User.query.all()
    return render_template('print_users.html', users = users)







@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + 
               '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', 
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])
