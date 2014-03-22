from app import app, db
import models
from flask import render_template, request, flash, redirect, jsonify
from sqlalchemy import create_engine
from forms import LoginForm, UserForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# User Related Views ---------------------------------------------------------

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

<<<<<<< HEAD
# Search Related Views ---------------------------------------------------------

@app.route('/results')
def results():
    return render_template('search_results.html')
=======

# Recipe Related Views -------------------------------------------------------

@app.route('/new_recipe', methods = ['GET', 'POST'])
def new_recipe():
    form = UserForm()
    if form.validate_on_submit():
        user = models.User(first_name = form.first.data,
                           last_name = form.last.data,  
                           email = form.email.data)
        db.session.add(user)
        db.session.commit()

        flash(user.first_name + " " + user.last_name + " created!")
    return render_template('new_user.html', form = form)



>>>>>>> 31b83d677390b3057c340d92931c8c8aa83e8215

@app.route('/send_fake_json')
def send_fake_json():
    data = [{"name": "PBJ", "image": "http://lh5.ggpht.com/Cc2dlo4nRsMJcp27oHlDIWB8anQ9gTJ-nQzJC9zRu4m3Zob8oG1pS1McaU3Sfm7uGMiUaVtKMAswyq3Br4TKmv0=s230-c" },
    {"name": "Pizza", "image": "http://lh5.ggpht.com/Cc2dlo4nRsMJcp27oHlDIWB8anQ9gTJ-nQzJC9zRu4m3Zob8oG1pS1McaU3Sfm7uGMiUaVtKMAswyq3Br4TKmv0=s230-c" },
    {"name": "Cheeseburger", "image": "http://lh5.ggpht.com/Cc2dlo4nRsMJcp27oHlDIWB8anQ9gTJ-nQzJC9zRu4m3Zob8oG1pS1McaU3Sfm7uGMiUaVtKMAswyq3Br4TKmv0=s230-c" }]
    return jsonify(data=data)


