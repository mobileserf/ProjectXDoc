#! /usr/bin/python

import os, sys
from pprint import pprint
import json


#adding Food Group
class FGDetails(object): 
       def __init__(self, name):
            self.name = name;
            self.foodId = list(); #list of foods in this group

       def appendFood(self, foodId):
           self.foodId.append(int(foodId))
       def printDetails(self, space):
           print space*' ', "name: ", self.name, "foodid: ";
           space +=4; 
           print space*' ', self.foodId

class FoodGroup(object):
       def __init__(self):
           self.fgDetails= dict();
           self.fgNameIdMap= dict();
           self.setDefaults();

       def setValue(self, id, name):
           self.fgDetails[id] = FGDetails(name);
           self.fgNameIdMap[name] = id;

       def setDefaults(self):
           self.setValue(0100000, "Branded Food Products Database")

       def getId(self, name):
           return self.fgNameIdMap[name];

       def setFoodId(self, groupId, foodId):
           self.fgDetails[groupId].appendFood(foodId);

       def retrieveAllFoodGroup(self, filename):
           data_file=open(filename)
           data = json.load(data_file)
           f_list=data['list']
           for k in f_list['item']:
              self.setValue(k['id'], k['name']);
           
       def printDetails(self, space=0):
           for id, fg in self.fgDetails.items():
              print space*' ', "id: ", id
              fg.printDetails(space);

