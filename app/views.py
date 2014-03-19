from app import app, db
import models
from flask import render_template, request, flash, redirect
from sqlalchemy import create_engine
from forms import LoginForm, UserForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/new_user', methods = ['GET', 'POST'])
def new_user():
    form = UserForm()
    if form.validate_on_submit():
        user = models.User(first_name = form.first.data,
                           last_name = form.last.data,  
                           email = form.email.data)
        db.session.add(user)
        db.session.commit()

        flash(user.first_name + " " + user.last_name + " created!")
    return render_template('new_user.html', form = form)


@app.route('/delete_user/<email>')
def delete_user(email):
    users = models.User.query.filter_by(email=email)
    for user in users:
        db.session.delete(user)
        db.session.commit()
        flash(user.first_name + " " + user.last_name + " deleted!")
    return redirect('/index')


@app.route('/get_users')
def get_users():
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
