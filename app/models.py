from app import db
from sqlalchemy.ext.declarative import declarative_base

# The values for a user's access level
ROLE_USER = 0
ROLE_ADMIN = 1

# Each class represents a table in the database
Base = declarative_base()
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(4000), unique = True)
    last_name = db.Column(db.String(4000), unique = True)
    email = db.Column(db.String(4000), unique = True)
    recipes = db.relationship('Recipe', backref = 'author', lazy = 'dynamic')
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.first_name + " " + self.last_name)

RecipeIngredients = db.Table('RecipeIngredients', Base.metadata,
	db.Column('id', db.Integer, primary_key = True),
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')),
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.id')),
   	db.Column('amount', db.Integer),
    db.Column('units', db.String(4000))
)
Recipe = db.Table('Recipe', Base.metadata,
	db.Column('id', db.Integer, primary_key = True),
    db.Column('name', db.String(4000), unique = True),
    db.Column('difficulty', db.Integer),
    db.Column('time', db.Integer),
    db.Column('servings', db.Integer),
    db.Column('instructions', db.String(4000)),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)
Ingredient = db.Table('Ingredient', Base.metadata,
	db.Column('id', db.Integer, primary_key = True),
   	db.Column('name', db.String(4000), unique = True)
)
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(4000), unique = True)
    difficulty = db.Column(db.Integer)
    time = db.Column(db.Integer)
    servings = db.Column(db.Integer)
    instructions = db.Column(db.String(4000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ingredients = db.relationship("Ingredient",secondary=RecipeIngredients,backref="recipes")

    def __repr__(self):
        return '<Recipe %r>' % (self.name)

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(4000), unique = True)
    recipes = db.relationship(Recipe, secondary=RecipeIngredients,backref="ingredients")

    def __repr__(self):
        return '<Ingredient %r>' % (self.name)


class RecipeIngredients(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'))
    amount = db.Column(db.Integer)
    units = db.Column(db.String(4000))

    def __repr__(self):
        return '<Post %r>' % (self.recipe_id + " : " + self.ingredient_id)

