from app import app, db
import models


def get_ingredient_ids():
	ingredients = models.Ingredient.query.all()
	list = []
	for ingredient in ingredients:
		list.append(ingredient.id)







