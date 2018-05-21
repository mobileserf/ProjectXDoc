#! /usr/bin/python

import json
import sys
from pprint import pprint

file_name=sys.argv[1]
data_file=open(file_name)
data = json.load(data_file)

f_list=data['list']
print f_list["total"]
