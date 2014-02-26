from app import app
from flask import render_template, request

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


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





