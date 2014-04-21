from app import db 
from sqlalchemy.ext.declarative import declarative_base

# The values for a user's access level
ROLE_USER = 0
ROLE_ADMIN = 1



# Many to Many table for likes
likes = db.Table('likes',
                 db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                 db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id'))
                 )



# Each class represents a table in the database
Base = declarative_base()
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(4000), unique = False)
    last_name = db.Column(db.String(4000), unique = False)
    has_image = db.Column(db.Boolean, default=False)
    #image = db.Column(db.String(4000), unique = False)
    email = db.Column(db.String(4000), unique = True)
    recipes = db.relationship('Recipe', backref = 'author', lazy = 'dynamic')
    likes = db.relationship('Recipe', secondary = likes,
                                  backref = db.backref('likes', lazy = 'dynamic'))
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return unicode(self.id)
    
    def like(self, recipe):
        self.likes.append(recipe)
        db.session.merge(self)
        return self
    
    def add_recipe(self, recipe):
        if not self.is_recipe(recipe):
            self.recipes.append(recipe)
            db.session.merge(self)
            return self
    
    def remove_recipe(self, recipe):
        if self.is_recipe(recipe):
            self.recipes.remove(recipe)
            db.session.merge(self)
            return self
    
    def is_recipe(self,recipe):
        return self.recipes.filter(Recipe.id == recipe.id).count()

    def __repr__(self):
        return '<User %r>' % (self.first_name + " " + self.last_name)




# Many to Many table for recipe to ingredient
ingredients = db.Table('ingredients',
            db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')),
            db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.id')),
            db.Column('quantity', db.Integer),
            db.Column('measurement', db.String(4000), unique = False)
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
    image = db.Column(db.String(4000), unique = False)
    
    ingredients = db.relationship('Ingredient', secondary = ingredients,
                        backref = db.backref('recipes', lazy = 'dynamic'))
                        
                        
                        
    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
        db.session.merge(self)
        return self


    def __repr__(self):
        return '<Recipe %r>' % (self.name)



# Ingredient Table
class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(4000), unique = True)

    def __repr__(self):
        return '<Ingredient %r>' % (self.name)


