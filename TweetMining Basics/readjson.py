import json
from pprint import pprint

with open('python.json') as json_data:
    d = json.loads(json_data)
    json_data.close()
    pprint(d)