from pymongo import MongoClient

client = MongoClient()

db = client.lab3

print(list(db.people.find()))