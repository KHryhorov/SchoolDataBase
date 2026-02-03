import csv
with open("config.txt","r") as config:
    min_score=int(config.read())

print(min_score)