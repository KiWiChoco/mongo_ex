from pymongo import MongoClient
from pprint import pprint
import pymongo
from bson.son import SON

client = MongoClient()

db = client.lab7

db.shelter.drop_indexes()

db.shelter.create_index([("province",pymongo.TEXT)])

cur = db.shelter.aggregate([{"$group":{"_id":{"province":"$province"},
                                       "avg_occupancy":{"$avg":"$occupancy"},
                                       "count":{"$sum":1}
                                       }},
                            {"$project":{"_id.province":1,"_id.city":1,"count":1,"avg_occupancy":1}}
                            ])

for e in cur:
    pprint(e)