from pymongo import MongoClient,GEOSPHERE
from pprint import pprint
import math

client = MongoClient()
db = client.lab6

# pprint(db.states.find_one({"name":"California"})["loc"]["coordinates"])

quary_box = db.states.find_one({"name":"California"})["loc"]

# pprint(db.airports.find({"loc.coordinates":{"$geoWithin":{"$geometry":quary_box}}}))

airports = db.airports.find({"loc.coordinates":{"$geoWithin":{"$geometry":quary_box}}})

sfo_coordinates = set()
airports_coordinates = set()
distance_list = []
sfo_coordinates.add(db.airports.find_one({'code':"SFO"})["loc"]["coordinates"])

for airport in airports:
    #print(airport)
    airports_coordinates.add(airport["loc"]["coordinates"])

# def ucli(co1,co2):
#     distance = math.sqrt((float(co2[0])-float(co1[0]))**2 + (float(co2[1])-float(co1[1]))**2)
#     distance_list.append(distance)
#
# for i in range(len(airports_coordinates)):
#     ucli(airports_coordinates[i],sfo_coordinates)

# sort_distance = distance_list.sort()
# print(sort_distance[-2])

print(airports_coordinates)
print(sfo_coordinates)