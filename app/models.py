from app import db

# The values for a user's access level
ROLE_USER = 0
ROLE_ADMIN = 1

# Each class represents a table in the database

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(64), unique = True)
    last_name = db.Column(db.String(64), unique = True)
    email = db.Column(db.String(120), unique = True)
    recipes = db.relationship('Recipe', backref = 'author', lazy = 'dynamic')
    role = db.Column(db.SmallInteger, default = ROLE_USER)

    def __repr__(self):
        return '<User %r>' % (self.first_name + " " + self.last_name)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    ingredients = db.Column(db.String(140))
    instructions = db.Column(db.String(140))
    time = db.Column(db.Integer)
    category = db.Column(db.String(140))
    servings = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.name)

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)

    def __repr__(self):
        return '<Post %r>' % (self.name)

class RecipeIngredients(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'))
    amount = db.Column(db.Integer)
    units = db.Column(db.String(140))

    def __repr__(self):
        return '<Post %r>' % (self.recipe_id + " : " + self.ingredient_id)

