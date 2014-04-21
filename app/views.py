from app import app, db, lm, oid
import models, os
from models import User, ROLE_USER, ROLE_ADMIN, Recipe, Ingredient
from flask import render_template, request, flash, redirect, session, url_for, request, g, jsonify, send_from_directory, send_file
from flask.ext.login import login_user, logout_user, current_user, login_required
from sqlalchemy import create_engine, func
from forms import LoginForm, SearchForm, RecipeForm, EditUserForm, IngredientForm
from flask.ext.wtf import Form
from wtforms import SelectMultipleField
from sqlalchemy import or_
from config import PROFILE_IMAGE_PATH, RECIPE_IMAGE_PATH

@app.route('/')
@app.route('/index')
#@login_required
def index():
    user = g.user
    results = Recipe.query.order_by(func.random()).limit(20)
    return render_template('index.html', recipes = results)


@app.route('/test_index')
#@login_required
def test_index():
    user = g.user
    return render_template('test_index.html')


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
                             ask_for = ['nickname', 'email', 'fullname', 'image'])
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
        image = resp.image
        
        if fullname is not None:
            firstname = fullname.split(' ')[0]
            lastname = fullname.split(' ')[1]
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        if image is None or image == "":
            image = "http://upload.wikimedia.org/wikipedia/commons/0/02/Stickman.gif"

        user = User(first_name = firstname, last_name = lastname, image = image, email = resp.email, role = ROLE_USER)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/<email>')
def user(email):
    user = User.query.filter_by(email = email).first()
    if user == None:
        flash('User ' + email + ' not found.')
        return redirect(url_for('index'))

    #Recipes the user has created
    user_recipes = Recipe.query.filter_by(user_id = user.id)

    #Recipes the user has liked
    user_likes = Recipe.query.filter_by(user_id = user.id)

    #Recipes suggested for the user
    user_suggested = Recipe.query.order_by(func.random()).limit(20)
    
    return render_template('user.html', user = user, user_recipes = user_recipes, user_likes = user_likes, user_suggested = user_suggested)



@app.route('/edit_user', methods = ['GET', 'POST'])
@login_required
def edit_user():
    form = EditUserForm()
    
    if form.validate_on_submit():
        g.user.first_name = form.first_name.data
        g.user.last_name = form.last_name.data
        if form.image:
            form.image.data.save(os.path.join(PROFILE_IMAGE_PATH, '%d.jpg' % g.user.id))
            g.user.image = "/uploads/profile_images/%d.jpg"% g.user.id
        db.session.merge(g.user)
        db.session.commit()
        flash('Your profile has been updated')
        return redirect(url_for('index'))

    else:
        form.first_name.data = g.user.first_name
        form.last_name.data = g.user.last_name

    return render_template('edit_user.html', title = 'Edit Profile', form = form, user = g.user, action = 'Update')


@app.route('/uploads/profile_images/<filename>')
def send_pimage(filename):
    return send_from_directory(PROFILE_IMAGE_PATH, filename)

@app.route('/new_user', methods = ['GET', 'POST'])
def new_user():
    form = UserForm()
    if form.validate_on_submit():
        user = models.User(first_name = form.first_name.data,
                           last_name = form.last_name.data,
                           image = form.image.data)
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


# Recipe Related Views -------------------------------------------------------

@app.route('/new_recipe', methods = ['GET', 'POST'])
def new_recipe():
    
    class IngredientSelector(Form):
        ingredients = models.Ingredient.query.order_by(models.Ingredient.name.asc())
        choices = []
        for each in ingredients:
            choices.append((str(each.id), each.name))

        ingredient = SelectMultipleField(u'Ingredients', choices = choices)

    form = RecipeForm()
    selector = IngredientSelector()
    rid = models.Recipe
    if form.validate_on_submit():
        recipe = models.Recipe(
                name = form.name.data,
                difficulty = form.difficulty.data,
                time = form.time.data,
                servings = form.servings.data,
                instructions = form.instructions.data,
                user_id = g.user.get_id(),
                image = form.image.data
        )
        if form.image:
            form.image.data.save(os.path.join(RECIPE_IMAGE_PATH, '%s.jpg' % recipe.name))
            recipe.image = "/uploads/recipe_images/%s.jpg"% recipe.name

        if Recipe.query.filter_by(name = recipe.name).count() > 0:
            flash('A recipe with this name already exists!');
            return render_template('new_recipe.html', form = form, selector = selector)
        
        db.session.add(recipe)
        db.session.commit()
        
        selected_ingredients = selector.ingredient.data

        for each in selected_ingredients:
            i = Ingredient.query.get(each)
            recipe.add_ingredient(i)

        db.session.commit()

        flash(recipe.name + ' created!')
        return redirect(url_for('user', email = g.user.email))

    flash('A field in the recipe form was invalid!')
    return render_template('new_recipe.html', form = form, selector = selector)


@app.route('/uploads/recipe_images/<recipeimage>')
def send_rimage(recipeimage):
    return send_from_directory(RECIPE_IMAGE_PATH, recipeimage)

@app.route('/new_ingredient', methods = ['GET', 'POST'])
def new_ingredient():
    form = IngredientForm()
    
    if form.validate_on_submit():
        ingredient = models.Ingredient(name = form.name.data)
        
        if Ingredient.query.filter_by(name = ingredient.name).count() > 0:
            flash('A recipe with this name already exists!');
            return render_template('new_ingredient.html', form = form)
        
        db.session.add(ingredient)
        db.session.commit()
        
        flash(ingredient.name + ' added!')
        return render_template('new_ingredient.html', form = form)
    
    flash('Problem with the form!')
    return render_template('new_ingredient.html', form = form)



@app.route('/get_recipes')
def get_recipes():
    recipes = models.Recipe.query.all()
    return render_template('print_name.html', objects = recipes)



@app.route('/get_ingredients')
def get_ingredients():
    ingredients = models.Ingredient.query.all()
    return render_template('print_name.html', objects = ingredients)



@app.route('/get_results', methods=['POST'])
def search_results():
    form = SearchForm()
    '''if not form.validate_on_submit():
        flash("Please enter something to search for!")
        return redirect('/index')'''
    
    byname = Recipe.query.filter(Recipe.name.like('%'+form.search.data.lower()+'%'))
    byingredient = Recipe.query.filter(Recipe.ingredients.any(Ingredient.name.like('%'+form.search.data.lower()+'%'))).all()
    
    # combine 2 results above!!!
    combinedResults = []
    rids = []
    for i in byname:
    	if (i.id not in rids):
    		rids.append(i.id);
    		combinedResults.append(i)
    	
    for i in byingredient:
    	if (i.id not in rids):
    		rids.append(i.id);
    		combinedResults.append(i)


    if byname == None:
        flash("No recipes with that name!")
    
    if byingredient == None:
        flash("No recipes with that ingredient!")
    
    return render_template('search_results.html', results = combinedResults)




@app.route('/test', methods = ['GET', 'POST'])
def test():
    form = IngredientSelector()
    if form.validate_on_submit():
        options = form.ingredient.data
        for each in options:
            flash(each)
        return redirect('/test')
    return render_template('test.html', form = form)
