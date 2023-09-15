import json
import os

path = './res/papers.json'
full_papers = set()

 
with open(path, 'r') as f:
        papers = json.load(f)
        full_papers = full_papers | {paper['Title'] for paper in papers}

with open('.github/citation/citation.json', 'r') as f:
    table = json.load(f)

for key in list(table.keys()):
    if key not in full_papers:
        table.pop(key)

for paper in full_papers:
    if paper not in table:
        table[paper] = {'citation': 0, 'last update': '2016-04-08'}

with open('.github/citation/citation.json', 'w') as f:
    json.dump(table, f)
