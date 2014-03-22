from app import app, db
import models


def get_ingredient_ids():
	ingredients = models.Ingredient.query.all()
	list = []
	for ingredient in ingredients:
		list.append(ingredient.id)
	return list

def get_ingredients(recipe_id):
	return models.RecipeIngredients.query.filter_by(id=recipe_id)

def ingredients_to_binary_array(recipe_id):
	number_of_ingredients = len(models.Ingredient.query.all())
	ingredients_in_recipe = get_ingredients(recipe_id)
	binary_array = []

	for i in range(1, number_of_ingredients):
		if i in ingredients_in_recipe:
			binary_array.append(1)
		else:
			binary_array.append(0)
	return binary_array

	


