from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    userid = db.Column(db.Integer, primary_key = True)
    first = db.Column(db.String(64), index = True, unique = True)
    last = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)

    def __repr__(self):
        return '<User %r>' % (self.first + " " + self.last)

class Recipe(db.Model):
    rid = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True, unique = True)
    difficulty = db.Column(db.Integer, primary_key = True)
    time = db.Column(db.Integer, primary_key = True)
    instructions = db.Column(db.Text, index = True, unique = True)

    def __repr__(self):
        return '<User %r>' % (self.name)

class Ingredients(db.Model):
    ingid = db.Column(db.Integer, primary_key = True)
    ingredients = db.Column(db.String(64), index = True, unique = True)
   
    def __repr__(self):
        return '<User %r>' % (self.ingredients)






