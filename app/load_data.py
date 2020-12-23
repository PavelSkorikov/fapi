import json
from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017/")
db = client["base"]
Collection = db["employee"]

with open('employees.json') as file:
    file_data = json.load(file)

Collection.insert_many(file_data)