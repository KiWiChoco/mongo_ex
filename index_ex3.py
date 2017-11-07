from pymongo import MongoClient
import sys

client = MongoClient()

db = client.lab5

# var1 = sys.argv[1] 터미널에서 실행하기 위해서 쓴 변수
# var2 = sys.argv[2]
# var3 = sys.argv[3]

def weak(po1,po2,po3):
    po1_weak = set(db.pokedex.find_one({"name":"%s"%po1})["weaknesses"])
    po2_weak = set(db.pokedex.find_one({"name":"%s"%po2})["weaknesses"])
    po3_weak = set(db.pokedex.find_one({"name":"%s"%po3})["weaknesses"])

    weakness = po1_weak & po2_weak & po3_weak

    output(weakness)


def output(weakness):
    weakness_len = len(list(weakness))

    pokemon = set()

    for num in range(1,152):
        # num_weak = set(db.pokedex.find_one({"id":num})["weaknesses"])
        # #print(num_weak)
        if set(db.pokedex.find_one({"id":num})["weaknesses"]) & weakness:
            pokemon.add(num)

    pokemon_names = []

    for i in pokemon:
        name = db.pokedex.find_one({"id":i})["name"]
        pokemon_names.append(name)

    print(len(pokemon_names))
    sort_names = sorted(pokemon_names)

    for name in sort_names:
        print(db.pokedex.find_one({"name":"%s"%name},{"id":1,"name":1,"type":1,"_id":0}))




#print(db.pokedex.find_one({"id":1})["weaknesses"])

#weak(var1,var2,var3) -> 터미널에서 실행하기 위해 필요
#python index_ex3.py Scyther Vileplume Butterfree  --> 파이썬 파일이 있는 디렉토리로 들어가서 터미널에서 이 명령어 실행하면 됨

weak("Scyther","Vileplume","Butterfree")

