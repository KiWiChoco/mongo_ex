from pymongo import MongoClient

client = MongoClient()

db = client.lab4

# k = input("please write:")

def insert():
    try:
        txt = {"_id":4,"item":{"category":"Camera","type":"Digital"},"amount":15}
        db.sales.insert(txt)

    except Exception as e:
        print(e)


# txt = {"_id":2,"name":"zoe"}
#
# print(txt["_id"])

insert()