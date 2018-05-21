#! /usr/bin/python

import json
import sys
from pprint import pprint

file_name=sys.argv[1]
#"list_f_501"
print file_name
data_file=open(file_name)
data = json.load(data_file)

f_list=data['list']
print f_list["start"]
print f_list["end"]
print f_list["total"]
#items=len(f_list['item'])
#print items
for k in f_list['item']:
    print( '{} = {}').format(k["id"],k['name']) 

print f_list["start"]
print f_list["end"]
print f_list["total"]
