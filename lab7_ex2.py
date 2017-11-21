from pymongo import MongoClient
from pprint import pprint
import pymongo

client = MongoClient()

db = client.lab7

db.shelter.drop_indexes()

db.shelter.create_index([("province",pymongo.TEXT)])

#pprint(db.shelter.index_information())

cur = db.shelter.find({"$text":{"$search":"강원도"},"occupancy":{"$gte":1000}},{"_id":0,"name":1})

for e in cur:
    pprint(e)