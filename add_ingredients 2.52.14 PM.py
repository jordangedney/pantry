# This program needs to be run in the highest level directory, and
# requires the file 'common_ingredients' to be in the same directory


# Keep .pyc files from being generated
import sys
sys.dont_write_bytecode = True

from app import db, models

lines = [line.strip() for line in open('common_ingredients')]
lines = [line.title() for line in lines]

for each in lines:
	ingredient = models.Ingredient(name = each)
	db.session.add(ingredient)
	db.session.commit()