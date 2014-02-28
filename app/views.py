from app import app
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


@app.route('/recipe')
def recipe():
    recipes = [ # fake recipes, until quereying works
        { 
            'name': 'Egg Sandwich', 
            'ingredients': { 
            				'eggs': '2',
            				'bread': '2',  
            				}, 
           	'time': '10'
        },
        { 
            'name': 'PBJ', 
            'ingredients': { 
            				'peanut butter': '2',
            				'jelly': '2',
            				'bread': '2',  
            				}, 
           	'time': '5'
        }
    ]
    return render_template('recipe.html', recipes=recipes)







