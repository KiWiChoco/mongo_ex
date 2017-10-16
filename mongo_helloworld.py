from pymongo import MongoClient


def main():
    client = MongoClient()

    txt = {"Author":"Joo","Text":"Hello world!"}
    db = client.lab2
    db.posts.insert_one(txt)
    print(db.posts.find_one())


if __name__ == "__main__":
    main()
