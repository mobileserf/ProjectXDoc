#! /usr/bin/python

#import nutrition_pb2
import os, sys
from pprint import pprint
import json

class MultiIndex:
       def __init__(self):
            self.FirstSecond=dict();
            self.SecondFirst=dict();
       def addOne(self, dictionary, first, second):
           value = dictionary.get(first, None);
           if value is None:
               dictionary[first] = second;
           elif value != second: 
              print( 'Err: Value Already present key: {} value: {}, old_value {} ').format(first, second, value);
              sys.exit(-1);

       def add(self, first, second):
           self.addOne(self.FirstSecond, first, second); 
           self.addOne(self.SecondFirst, second, first);

       def getKey(self, value):
           return self.SecondFirst.get(value, None) 

       def getValue(self, key):
           return self.FirstSecond.get(key, None) 
       
       def getSize(self):
           return len(self.FirstSecond) 
       

       def printDetails(self):
           for id, fg in self.FirstSecond.items():
             print( '{} = {}').format(id, fg)

# NutritionMap map<id, NGDetails>
class  ParseList(MultiIndex):
       def getList(self, filename):
           data_file=open(filename)
           data = json.load(data_file)
           f_list=data['list']
           for k in f_list['item']:
              self.add(int(k["id"]), k['name'].encode('utf-8').strip());
                      
       def getListStringKey(self, filename):
           data_file=open(filename)
           data = json.load(data_file)
           f_list=data['list']
           for k in f_list['item']:
              self.add(k["id"], k['name'].encode('utf-8').strip());
