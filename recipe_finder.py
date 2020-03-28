from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.recipe_database
recipe_dictionary = db.recipe_collection