from pymongo import MongoClient
from pprint import pprint
import pymongo

client = MongoClient()

db = client.lab5

#1
pprint(db.pokedex.find({"name":"Wartortle"}).explain()['executionStats'])

#2
db.pokedex.create_index("name")

print("-"*80)

#3
pprint(db.pokedex.find({"name":"Wartortle"}).explain()['executionStats'])

#4
db.pokedex.create_index([('id',pymongo.DESCENDING),('name',pymongo.ASCENDING)])

#5
db.pokedex.drop_indexes()