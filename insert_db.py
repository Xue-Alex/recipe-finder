import pymongo
import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.recipe_database
collection = db.recipe_collection

with open('full_format_recipes.json') as f:
    d = json.load(f)
    for recipe in d:
        collection.insert_one(recipe)

