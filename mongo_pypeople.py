from pymongo import MongoClient

def main():
    client = MongoClient()

    txt = [{"name": "Kim", "age": 21},
             {"name": "Lee", "age": 22},
             {"name": "Park", "age": 27, "skills": [ "mongodb", "python"]},
             {"name": "Choi", "age": 22, "score": 10 }]

    db = client.lab2
    db.pypeople.insert_many(txt)

    peoples = db.pypeople.find()
    for people in peoples:
        print(people)
    client.close()

if __name__ == "__main__":
    main()

