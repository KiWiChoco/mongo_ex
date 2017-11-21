from pymongo import MongoClient,GEOSPHERE
from pprint import pprint
import pymongo
from bson.son import SON

client = MongoClient()

db = client.lab7

db.shelter.drop_indexes()

#db.shelter.create_index([("province",pymongo.TEXT)])

db.shelter.create_index([("location",GEOSPHERE)])

cur = db.shelter.aggregate([{"$geoNear":{
                                    "near":{"type":"Point","coordinates":[129.630170,35.689834]},
                                    "distanceField":"distance",
                                    "maxDistance":20000,
                                    "spherical":True
                                    }
                            },
                    {"$group": {"_id": {"province": "$province"},
                            "sum_occupancy": {"$sum": "$occupancy"},
                                "count": {"$sum": 1},
                            "avg_distancefromsea": {"$avg":"$distancefromsea"}
                                }},
                    {"$project": {"_id.province": 1,"count": 1, "sum_occupancy": 1,"avg_distancefromsea":1}}
                            ])

for e in cur:
    print(e)