import json
import sys
from pprint import pprint
from elasticsearch import Elasticsearch

es = Elasticsearch(['localhost'], port=9200)

data = json.load(open("/media/minchao/3gpp_search_engine/doc/f23401.json", "r"))

for i, line in enumerate(data):
    if len(line['desc']) < 1000000:
        #print(len(line['desc']))
        es.index(index='f23401', doc_type='doc', id=i, body=line)
