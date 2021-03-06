from app import app, db, models


def get_ingredient_ids():
	ingredients = models.Ingredient.query.all()
	list = []
	for ingredient in ingredients:
		list.append(ingredient.id)
	return list

def get_ingredients(recipe_id):
	return Ingredient.query.filter(Ingredient.recipes.any(id=recipe_id))

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


def number_of_shared_ingredients(first_id, second_id):
	ingredients_in_first = get_ingredients(first_id)
	ingredients_in_second = get_ingredients(second_id)
	array_first = ingredients_to_binary_array(ingredients_in_first)
	array_second = ingredients_to_binary_array(ingredients_in_second)

	shared_ingredients = 0
	for x in range(len(array_first)):
		first = array_first.pop()
		second = array_second.pop()
		if first == second:
			shared_ingredients += 1

	return shared_ingredients

def find_x_closest(recipe_id, number_of_recipes):
	recipes = models.Recipe.query.all()
	if recipe_id in recipes: recipes.remove(recipe_id)

	x_closest = []

	for i in range(number_of_recipes):
		 closest = find_closest(recipe_id, recipes)
		 x_closest.append(closest)
		 if closest in recipes: recipes.remove(closest)

	return x_closest

def find_closest(recipe_id, recipes):
	closest_id = 0
	closest_number = 0

	for each in recipes:
		number = number_of_shared_ingredients(recipe_id, each)
		if number >= closest_number:
			closest_number = number
			closest_id = each

	return closest_id
