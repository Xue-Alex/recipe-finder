#from recipe_finder import recipe_dictionary
import os
import json

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def find_matching_recipes(ingredient_list):
    
    with open(os.path.join(__location__, 'full_format_recipes.json') ) as f:
        recipe_dictionary = json.load(f)


    valid_recipes = []
    for recipe in recipe_dictionary:
        if 'ingredients' not in recipe:
            continue
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

    with open(os.path.join(__location__, 'full_format_recipes.json')) as f:
        recipe_dictionary = json.load(f)

    for recipe in recipe_dictionary:
        if recipe['title'] == title:
            return recipe
    
    #return recipe_dictionary.find_one({'title': title})



