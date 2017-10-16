from pymongo import MongoClient


def score(st):
    count = 0
    str_list = st.split("0")
    for i in str_list:
        if str:
            length = len(i)
            for j in range(1,length+1):
                count += j
    return count

score_list = []

f = open("grade.txt",'r')
lines = f.readlines()
for line in lines[1:]:
    strip_line = line.strip().replace(" ","")
    # print(strip_line)
    score_list.append(score(strip_line))


# print(score_list)

client = MongoClient()
db = client.lab2

for i in range(len(score_list)):
    txt = {"_id":i,"score":score_list[i]}
    db.student_score.insert_one(txt)

