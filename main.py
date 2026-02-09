import csv
from traceback import format_stack

with open("config.txt","r") as config:
    min_score=int(config.read())

students=[]
with open("students.csv","r",encoding="utf-8") as cvs:
    reader = list(csv.DictReader(cvs))
    for s in reader:
        s["score"]= int(s["score"])
        students.append(s)

retest_list=[]
for s in students:
    if s["score"]<min_score:
            retest_list.append(s)

with open("retest.csv","w",encoding="utf-8", newline="") as retest:
    fieldnames = ["id", "name", "surname", "score"]
    writer=csv.DictWriter(retest,fieldnames=fieldnames)
    writer.writeheader()
    for s in retest_list:
        writer.writerow(s)

import json
success_list=[]
for s in  students:
    if s["score"]>=min_score:
        success_list.append(s)
for s in success_list:
    s["passed"]=True

with open("best_students.json","w",encoding="utf-8") as file:
    json.dump(success_list, file , indent=2 , ensure_ascii=False)