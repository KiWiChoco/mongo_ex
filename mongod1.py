from pymongo import MongoClient

client = MongoClient('localhost',27017)

db = client.test

print(db)

posts = db.posts

post = {"author" : "Mike",
 "text" : "My first blog post!",
 "tags" : ["mongodb", "python", "pymongo"]}

posts.insert(post)

print(posts.find_one())