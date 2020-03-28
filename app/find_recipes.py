from recipe_finder import recipe_dictionary

def find_matching_recipes(ingredient_list):
    valid_recipes = []
    for recipe in recipe_dictionary.find():
        dont_add_to_list = False
        for ingredient in ingredient_list:
            contained = False
            for recipe_ingredient in recipe['ingredients']:
                if ingredient in recipe_ingredient:
                    contained = True
                    break
            if not contained:
                dont_add_to_list = True
                break
        if not dont_add_to_list:
            valid_recipes.append(recipe)
            if len(valid_recipes) >= 11:
                return valid_recipes
    return valid_recipes

def get_one_recipe(title):
    return recipe_dictionary.find_one({'title': title})



