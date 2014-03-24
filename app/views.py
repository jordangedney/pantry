from app import app, db, lm, oid
import models
from models import User, ROLE_USER, ROLE_ADMIN, Recipe
from flask import render_template, request, flash, redirect, session, url_for, request, g, jsonify
from flask.ext.login import login_user, logout_user, current_user, login_required
from sqlalchemy import create_engine
from forms import LoginForm, UserForm, SearchForm, RecipeForm


@app.route('/')
@app.route('/index')
#@login_required
def index():
    user = g.user
    return render_template('index.html')

# User Related Views ---------------------------------------------------------

@app.route('/login', methods = ['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login('https://www.google.com/accounts/o8/id',
                ask_for = ['nickname', 'email'], ask_for_optional=['fullname'])
    return render_template('login.html', title = 'Sign In', form = form)


@app.before_request
def before_request():
    g.user = current_user


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email = resp.email).first()
    if user is None:
        nickname = resp.nickname
        fullname = resp.fullname
        if fullname is not None:
            firstname = fullname.split(' ')[0]
            lastname = fullname.split(' ')[1]
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(first_name = firstname, last_name = lastname, email = resp.email, role = ROLE_USER)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/<email>')
@login_required
def user(email):
    user = User.query.filter_by(email = email).first()
    if user == None:
        flash('User ' + nickname + ' not found.')
        return redirect(url_for('index'))
    
    return render_template('user.html', user = user)


@app.route('/new_user', methods = ['GET', 'POST'])
def new_user():
    form = UserForm()
    if form.validate_on_submit():
        user = models.User(first_name = form.first_name.data,
                           last_name = form.last_name.data)
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


# Search Related Views -------------------------------------------------------

@app.route('/new_recipe', methods = ['GET', 'POST'])
def new_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe = models.Recipe(name = form.name.data,
                           ingredients = form.ingredients.data,  
                           instructions = form.instructions.data,
                           time = form.time.data,
                           category = form.category.data,
                           servings = form.servings.data,
                           user_id = g.user.get_id()
                           )
        db.session.add(recipe)
        db.session.commit()

        flash(recipe.name + " created!")
        return redirect('/index')
    return render_template('new_recipe.html', form = form)

@app.route('/get_recipes')
def get_recipes():
    recipes = models.Recipe.query.all()
    return render_template('print_recipes.html', recipes = recipes)


@app.route('/get_results', methods=['POST'])
def search_results():
    form = SearchForm()
    #if not form.validate_on_submit():
    #    flash("Please enter something to search for!")
    #    return redirect('/index')
    
    #results = models.Recipes.query.filter_by(ingredient = form.search.data)   
    results = [{"name": "PBJ", "image": "http://lh5.ggpht.com/Cc2dlo4nRsMJcp27oHlDIWB8anQ9gTJ-nQzJC9zRu4m3Zob8oG1pS1McaU3Sfm7uGMiUaVtKMAswyq3Br4TKmv0=s230-c" },
    {"name": "Pizza", "image": "http://lh5.ggpht.com/Cc2dlo4nRsMJcp27oHlDIWB8anQ9gTJ-nQzJC9zRu4m3Zob8oG1pS1McaU3Sfm7uGMiUaVtKMAswyq3Br4TKmv0=s230-c" },
    {"name": "Cheeseburger", "image": "http://lh5.ggpht.com/Cc2dlo4nRsMJcp27oHlDIWB8anQ9gTJ-nQzJC9zRu4m3Zob8oG1pS1McaU3Sfm7uGMiUaVtKMAswyq3Br4TKmv0=s230-c" }]
    
    return render_template('search_results.html', results = results)
