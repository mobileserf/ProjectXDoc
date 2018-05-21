#! /usr/bin/python

import json
import sys
from pprint import pprint
from random import randint
from shutil import copyfile

file_name=sys.argv[1]
dst=sys.argv[2]
src=sys.argv[3]
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
    print( '{} = {}').format(k["id"],(k['name']).encode('ascii', 'ignore')) 
    id=(randint(1,702))
    src_file=src + "/" + `id` + ".jpg"
    dst_file=dst + "/" + k["id"] + ".jpg"
    print( '{} = {}').format(src_file, dst_file)
    copyfile(src_file, dst_file)

print f_list["start"]
print f_list["end"]
print f_list["total"]
