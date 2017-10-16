from pymongo import MongoClient
import datetime

client = MongoClient('localhost',27017)
# client = MongoClient()  <--localhost

print(client.database_names())  #데이터베이스 이름 출력

db = client.lab2

print(db.collection_names()) #데이터베이스 내의 컬랙션 이름 출력

collection = db.apples

post = {"author":"Mike","text":"My first blog post!",
        "tags":["MongoDB","Python","PyMongo"],"date":datetime.datetime.utcnow()}

db.lab2.inset_one(post)