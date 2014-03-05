from app import db

# Each class represents a table in the database

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(64), unique = True)
    last_name = db.Column(db.String(64), unique = True)
    email = db.Column(db.String(120), unique = True)
    recipes = db.relationship('Recipe', backref = 'author', lazy = 'dynamic')

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
        return '<Post %r>' % (self.body)




