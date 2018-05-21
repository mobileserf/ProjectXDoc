#! /usr/bin/python

#import nutrition_pb2
import os, sys
from pprint import pprint
import json

#/* single food name */

class Manufacture(object):
       def __init__(self, manufacture, commericalname):
           self.manufacture = manufacture;
           self.commericalname = commericalname;
           if len(commericalname) == 0:
              self.commericalname = manufacture;
           #if len(manufacture)  == 0:
           #   self.manufacture = commericalname;

       def isManuFacture(self):
           if self.manufacture == "":
              return False;
           return True;

       def printDetails(self, space ):
           print space*' ', "manufacture: " + self.manufacture 
           print space*' ', "commericalname  : " + self.commericalname 
               
class Manufactures(object):
       def __init__(self):
            self.manuFId = 0;
            self.manufactures=dict();
            #tmp value to hold manu name, id
            self.manuNameIdMap=dict();

       def add(self, manufacture, commericalname):
            man = Manufacture(manufacture, commericalname);
            if man.isManuFacture() == True:
               if man.manufacture in self.manuNameIdMap:
                  return self.manuNameIdMap[man.manufacture]
               else:
                  self.manuFId += 1;
                  self.manuNameIdMap[man.manufacture] = self.manuFId;
                  self.manufactures[self.manuFId] = man
                  return self.manuFId; 
            return 0;  
 
       def printManufacture(self, manFId, space):
           self.manufactures[manFId].printDetails(space); 
       def printManufactures(self, space):
           print space*' ', "TotalManufactures: " , len(self.manufactures);
           for id, manu in self.manufactures.items(): 
              print space*' ', "ManufactureId : " , id
              manu.printDetails(space); 

gManufactures = Manufactures(); 

def printManuFactures(space=0):
    gManufactures.printManufactures(space);

class FoodName(object):
       def __init__(self, name, sd, foodGroupId, manFId):
           self.name = name.encode('ascii', 'ignore'); #unicode to ascii
           self.sd = sd;# /* short description */
           self.foodGroupId = int(foodGroupId);
           self.manFId = int(manFId);
           
       def printDetails(self, space ):
           #print space*' ', "name: " + self.name, "SD: " + self.sd, "gId: "+ self.foodGroupId;
           print space*' ', "name: " + self.name 
           print space*' ', "description  : " + self.sd 
           print space*' ', "groupId : " , self.foodGroupId 
           print space*' ', "ManufactureId : " , self.manFId
           if self.manFId != 0: 
              gManufactures.printManufacture(self.manFId, space)

#list of all foods
class FoodList(object):
       def __init__(self):
            self.foodName=dict();
       #def add(self, id, name, sd, foodGroupId):
       #    self.foodName[int(id)] = FoodName(name, sd, foodGroupId);
       def add(self, id, foodGroupId, jFood):
           manuFId = gManufactures.add(jFood['manu'], jFood['cn']);
           self.foodName[int(id)] = FoodName(jFood['name'], jFood['sd'], foodGroupId, manuFId);
       def get(self, id):
           #if id in self.foodName: 
           return self.foodName[id];
       def printDetails(self, space=0):
           print space*' ', "TotalFoods: " , len(self.foodName);
           for id, food in self.foodName.items():
              food.printDetails(space);


