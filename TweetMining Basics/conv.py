import csv
import json

csvfile = open('tweets.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames=('text','url')
reader = csv.DictReader(csvfile,fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')