from pymongo import MongoClient,GEOSPHERE
from pprint import pprint
import math

client = MongoClient()
db = client.lab6

# pprint(db.states.find_one({"name":"California"})["loc"]["coordinates"])

quary_box = db.states.find_one({"name":"California"})["loc"]

# pprint(db.airports.find({"loc.coordinates":{"$geoWithin":{"$geometry":quary_box}}}))

states = db.states.find({"loc":{"$geoIntersects":{"$geometry":quary_box}}})

db.airports.create_index([("loc",GEOSPHERE)])


for state in states:
    print("state name : ",state["name"],'\n'"state code : ",state["code"])


# near_airports = db.airports.find({"loc.coordinates":{"$near":{"$geometry":quary_box,"$maxDistance":20000}}})
#
# for near_airport in near_airports:
#     print(near_airport)

# print(quary_box)

type = quary_box["type"]
coor = quary_box["coordinates"]


near_airports = db.airports.find({"loc":{"$near":{"$geometry":{"type":"Point","coordinates":[-73.965355,40.782865]},"$maxDistance":20000}},"type":"International"})

for near_airport in near_airports:
    print(near_airport)