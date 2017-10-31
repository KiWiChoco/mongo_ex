from pymongo import MongoClient
import collections

client = MongoClient()

db = client.lab4

#print(list(db.grade.find()))

sid_list = []

for i in list(db.grade.find()):
    sid_list.append(i["sid"])

#print(sid_list)

counter = collections.Counter(sid_list)

dic = dict(counter)

unique_item = dict()

for k,v in dic.items():
    if v==2:
        unique_item[k]=v

print(type(list(unique_item.keys())[0]))

unique = list(unique_item.keys())[0]

db.grade.insert({"sid":unique,"type":"quiz","score":80})




