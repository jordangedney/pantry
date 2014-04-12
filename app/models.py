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
    image = db.Column(db.String(4000), unique = False)
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
    
    def add_recipe(self, recipe):
        if not self.is_recipe(recipe):
            self.recipes.append(recipe)
            return self
    
    def remove_recipe(self, recipe):
        if self.is_recipe(recipe):
            self.recipes.remove(recipe)
            return self
    
    def is_recipe(self,recipe):
        return self.recipes.filter(Recipe.id == recipe.id).count()

    def __repr__(self):
        return '<User %r>' % (self.first_name + " " + self.last_name)



# Many to Many table for recipe to ingredient
ingredients = db.Table('ingredients',
            db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')),
            db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.id'))
)


# Recipe Table
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(4000), unique = True)
    difficulty = db.Column(db.Integer)
    time = db.Column(db.Integer)
    servings = db.Column(db.Integer)
    instructions = db.Column(db.String(4000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    ingredients = db.relationship('Ingredient', secondary = ingredients,
                        backref = db.backref('recipes', lazy = 'dynamic'))
                        
                        
    def is_ingredient(self, ingredient):
        return Ingredient.query.filter(Ingredient.id == ingredient.id).count()
                        
    def add_ingredient(self, ingredient):
        if self.is_ingredient(ingredient):
            self.ingredients.append(ingredient)
        else:
            new_ingredient = Ingredient(name = ingredient.name)
            db.session.add(new_ingredient)
            db.session.commit()
        return self


    def __repr__(self):
        return '<Recipe %r>' % (self.name)



# Ingredient Table
class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(4000), unique = True)

    def __repr__(self):
        return '<Ingredient %r>' % (self.name)


