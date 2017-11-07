from pymongo import MongoClient
import collections

client = MongoClient()
#
# db = client.tt
#
# # print(list(db.grade.find({"sid":0}))[0]["type"])
#
# print(list(db.ex.find({"boo":100}))[0]["stat"])
#
# k=list(db.ex.find({"boo":100}))[0]["stat"]
#
# print(k)

db=client.project

# db.posts.deleteOne({"_id":4})
import pymongo


print(list(db.user.find({"_id":"zoo"}))[0]["followings"])