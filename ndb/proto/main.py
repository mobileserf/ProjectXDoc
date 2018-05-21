#! /usr/bin/python

#import nutrition_pb2
import os, sys
from pprint import pprint
import json
import foodgroup
import nutritionlist
import foodlist
import foodunits

class FoodMeasure(object):
       def __init__(self, value, gramEqv):
            self.value = value;
            self.gramEqv = gramEqv;
       def printDetails(self, space=0):
           print space*' ', "value: ", self.value, "gram equv: ", self.gramEqv

class FoodNutrient(object):
       def __init__(self , jNutriant):
           self.nutrientId = jNutriant['nutrient_id']
           self.unit = jNutriant['unit']
           self.measures = list();
           #add default measure
           value = jNutriant['value']
           if value == 0.0 or value == 0:
              measure = FoodMeasure(value, value);
              self.measures.append(measure);
           else:
              measure = FoodMeasure(value, value/100);
              self.measures.append(measure);
           #print measure.printDetails(4)   
           for k in jNutriant['measures']:
              if  k is not None:
                 measure = FoodMeasure(k['value'], k['eqv']);
                 self.measures.append(measure);
                 #print measure.printDetails(4)   
           #TODO remove
           #print "nutriantId: ", self.nutrientId;
           #print "measures: ", self.measures;

       def printDetails(self, space=0):
           global gNutritions;
           #print space*' ', "nutriantId: ", self.nutrientId 
           gNutritions.printNutrition(self.nutrientId, space);
           for measure in self.measures:
               measure.printDetails(space)


class Food(object):
       def __init__(self , jNutriants):
         global gunits;
         self.units = foodunits.MeasureLabels(gunits); # measure labels of food nutrition, this is same for all nutrition  
         self.nutritions = list(); #list of FoodNutrient for this food
         jFirstN =  jNutriants[0];
         self.units.append(1);
         global gunits; 
         for k in jFirstN['measures']:
             if  k is not None:
               #print k
               self.units.append(gunits.add(k['label']))
         for nutrition in jNutriants:
             nutriant = FoodNutrient(nutrition);
             self.nutritions.append(nutriant);
             #nutriant.printDetails(0)
       def printDetails(self, space):
           self.units.printDetails(space);
           for nutrition in self.nutritions:
              print ""
              nutrition.printDetails(space);


#contains map<id, Food>
class FoodDetails(object):
       def __init__(self):
            self.foodName=dict(); #map<id, Food>
            
       def add(self, jFood):
           global gfoodList; 
           global gFoodGroup; 
           ndbno = int(jFood['ndbno']);
           groupId = gFoodGroup.getId(jFood['fg']);
           gFoodGroup.setFoodId(groupId, ndbno);
           gfoodList.add(ndbno, groupId, jFood); 
           jNutri  = jFood['nutrients'];  
           fd = Food(jNutri);
           self.foodName[int(ndbno)] = fd;

       def getFoodDetails(self, filename):
           data_file=open(filename)
           data = json.load(data_file)
           f_report=data['report'];
           jFood = f_report['food'];
           self.add(jFood); 


       def getAllFoodDetails(self, path):
           dirs = os.listdir( path )
           for file in dirs:
              food = path + "/" + file
              #print "Reading " + food
              self.getFoodDetails(food);
         
       def printDetails(self):
           for id, food  in self.foodName.items():
              global gfoodList; 
              print "id: ", id;
              fn = gfoodList.get(id);
              fn.printDetails(4);
              food.printDetails(4);

       def printFood(self, id):
           global gfoodList; 
           food = self.foodName.get(id); 
           print "id: ",  id;
           fn = gfoodList.get(id);
           fn.printDetails(4);
           food.printDetails(4);


gBasePath="/home/ajose/work/wifi_auth/ndb"

gFoodListDir=gBasePath + "/list"

#get all food Group
gFoodGroupFile=gFoodListDir + "/list_g_0"
gFoodGroup = foodgroup.FoodGroup();
gFoodGroup.retrieveAllFoodGroup(gFoodGroupFile);

gNutritionFile=gFoodListDir + "/list_n_0"
gNutritions = nutritionlist.Nutritions();
gNutritions.getAllNutrition(gNutritionFile);
#gNutritions.printDetails()
#gNutritions.printNutrition(255, 0);

gfoodList = foodlist.FoodList();

#print  json.dumps(foods.__dict__);
#gFoodDir=gBasePath + "/food_test"
gFoodDir=gBasePath + "/food"

default_unit = "100 g"
gunits = foodunits.Units();
gunits.add(default_unit);
#gunits.printDetails()

foods = FoodDetails();
foods.getAllFoodDetails(gFoodDir);
#foods.printDetails()
#gFoodGroup.printDetails(0);
#gfoodList.printDetails(0);
foodlist.printManuFactures(0); 
#foods.printFood(22996);

#print  json.dumps(foods.__dict__);
# Main procedure:  Reads the entire address book from a file,
#   adds one person based on user input, then writes it back out to the same
#   file.
if len(sys.argv) != 1:
  print "Usage:", sys.argv[0] 
  sys.exit(-1)


print "hai"
