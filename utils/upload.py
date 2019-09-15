import json
import sys
from pprint import pprint
from elasticsearch import Elasticsearch

es = Elasticsearch(['localhost'], port=9200)

myFile = open("test.json", "r").read()
data = myFile.split('},')

json_str=""
docs = {}
i = 0

for line in data:
    startIndex = line.find('[') + 1
    endIndex = line.find(']')
    print(startIndex, endIndex);
    if(startIndex != 0):
        line = line[startIndex:] + '}'
    elif(endIndex != -1):
        line = line[:endIndex]
    else:
        line = line + '}'
    print(line)
    es.index(index='test', doc_type='doc', id=i, body=line)
    i = i + 1
