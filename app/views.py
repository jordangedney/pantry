from app import app
import models
from flask import render_template, request, flash, redirect
from sqlalchemy import create_engine
from forms import LoginForm



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


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


@app.route('/get_recipe')
def get_recipe():
    recipes = models.Recipe.query.all()
    return jsonify(recipes)







