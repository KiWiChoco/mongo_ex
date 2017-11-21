from pymongo import MongoClient
from pprint import pprint
import pymongo
from bson.son import SON

client = MongoClient()

db = client.lab7

db.shelter.drop_indexes()

db.shelter.create_index([("province",pymongo.TEXT)])

cur = db.shelter.aggregate([{"$match":{"$text":{"$search":"부산광역시"}}},{"$sort":SON([("name",1)])},{"$project":{"_id":0,"name":1,"address":1,"location":1}}])

for e in cur:
    pprint(e)