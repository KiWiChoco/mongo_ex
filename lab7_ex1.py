from pymongo import MongoClient
from pprint import pprint
import pymongo

client = MongoClient()

db = client.lab7


db.shelter.create_index([("province",pymongo.TEXT),("city",pymongo.TEXT)])

pprint(db.shelter.index_information())


