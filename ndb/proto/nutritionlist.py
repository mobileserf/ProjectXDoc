#! /usr/bin/python

#import nutrition_pb2
import os, sys
from pprint import pprint
import json

#/* nutrition Group info */
class  NutrientGroupId(object):
       def __init__(self):
            self.nutritionGId=dict();
       def add(self, id, name):
           self.nutritionGId[id] = name;

#/* nutrition info */
class  NGDetails(object):
       def __init__(self, name):
            self.name = name;
            self.nGId = 0; #/* NutrientGroupId , ex: Proximates id in NutrientGroupId*/
            self.unitId = 0; # /* g, kcal, kJ
       def addNutrientGroupId(self, id):
            self.nGId = id;
       def printDetails(self, id, space):
           print space*' ', "id:",  id, " gid: ", self.nGId, " name: " + self.name; 

# NutritionMap map<id, NGDetails>
class  Nutritions(object):
       def __init__(self):
            self.nutritions=dict();

       def add(self, id, name):
           ng = NGDetails(name); 
           self.nutritions[int(id)] = ng;

       def getAllNutrition(self, filename):
           data_file=open(filename)
           data = json.load(data_file)
           f_list=data['list']
           for k in f_list['item']:
              self.add(k["id"], k['name']);

       def printDetails(self, space=0):
           for id, nutrition in self.nutritions.items():
              nutrition.printDetails(id, space);

       def printNutrition(self, id, space=0):
           nutrition = self.nutritions.get(id);
           nutrition.printDetails(id, space);

                      

