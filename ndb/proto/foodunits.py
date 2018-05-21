#! /usr/bin/python

#import nutrition_pb2
import os, sys
from pprint import pprint
import json

#/* total unique units in food Group */
#Units map<id, name> & map<name, id> 
class Units(object):
       def __init__(self):
            self.units=dict();
            self.unitNameId=dict();
            self.unitId = 0;
       def add(self, name):
           name = name.encode('ascii', 'ignore') #unicode to ascii
           if name in self.unitNameId: 
              return self.unitNameId.get(name);
           else:
              self.unitId += 1
              self.units[self.unitId] = name;
              self.unitNameId[self.unitId] = id;
              return self.unitId;
       def getUnitName(self, id):
           return self.units.get(id);

       def printDetails(self, space=0):
           for id, name in self.units.items():
               print space*' ' , " id: ", id, " name: ", name;

#/*Food */
class MeasureLabels(object):
       def __init__(self, units):
            self.unitId=list();
            self.units = units;
       def append(self, id):
           self.unitId.append(int(id));
       def printDetails(self, space=0):
           global gunits; 
           for id in self.unitId:
              print space*' ', "unit id: " , id, " name: ", self.units.getUnitName(id);

