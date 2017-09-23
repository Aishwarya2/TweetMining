import json
from collections import Counter
fname = 'python.json'
with open(fname, 'r') as f:
 count_all = Counter()
 content = f.readlines()
 for line in content:
  tweet = json.loads(line)
  