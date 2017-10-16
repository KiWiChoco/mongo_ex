from pymongo import MongoClient

def main():
    client = MongoClient()

    db = client.lab2

    db.pypeople.update({"name":"Lee"},{"$set":{"name":"Lim","age":25}})
    db.pypeople.update({"name":"Kim"},{"$set":{"age":20}})
    db.pypeople.update({"name":"Park"},{"$unset":{"skills":""}})
    db.pypeople.update({"name":"Choi"},{"$inc":{"score":-2}})

    peoples = db.pypeople.find()
    for people in peoples:
        print(people)

    client.close()

if __name__ == "__main__":
    main()