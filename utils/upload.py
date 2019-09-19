import json
import sys
from pprint import pprint
from elasticsearch import Elasticsearch
import argparse
import ntpath

def main(file):
    name = ntpath.basename(file).split('.')[0]
    print(name)
    es = Elasticsearch(['localhost'], port=9200, timeout=50)
    data = json.load(open(file, "r"))

    for i, line in enumerate(data):
        if len(line['desc']) < 1000000:
            check_file = file + str(i)
            es.index(index=name, doc_type='doc', id=i, body=line)
        else:
            print("======================================")
            print(line['key'])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="input json file")
    parser.add_argument('--input', required='true')
    args = parser.parse_args()
    main(args.input)