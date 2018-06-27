#! /usr/bin/python

#import nutrition_pb2
import os, sys, glob
from pprint import pprint
import json
#import foodgroup
#import nutritionlist
#import foodlist
#import foodunits

#import parseList

#============================ FOOD MEAASURING LABEL START

class UniqueLabels(object):
       def __init__(self):
           self.labelId=dict(); #map<label, id>
           self.idLabel=dict(); #map<id, label>
           self.id = 0

       def getId(self, label):
           id = self.labelId.get(label, None)
           if id is None:
               self.id += 1;
               id = self.id 
               self.labelId[label] = id;
               self.idLabel[id] = label;
           #else:
           #   print "present id:", id, "label:", label;
           return id;
 
       def printDetails(self, space=0):
           for id, label  in self.idLabel.items():
              print space*' ', "id:", id, "label:", label;

uniqueLabels = UniqueLabels();

class FoodMeasure(object):
       def __init__(self, label, gramEqv, quantity):
            global uniqueLabels;
            self.label = label.encode('utf-8').strip();
            self.gramEqv = float(gramEqv);
            self.quantity = float(quantity);
            self.id = uniqueLabels.getId(self.label);
       def printDetails(self, space=0):
           print space*' ', "id: ", self.id,  "label: ", self.label, " gram equv: ", self.gramEqv, " quantity: ", self.quantity

#========================= FOOD MEAASURING LABEL END


class FoodNutrientDefault(object):
     def __init__(self, nutriantName, group, unit):
           self.group = group;
           self.unit = unit;
           self.nutriantName = nutriantName;

class FoodNutrientGroup(object):
       def __init__(self):
           self.nutriantGroup=dict(); #map<id, Default>

       def isDefault(self, nutriantId, nutriantName, group, unit):
           value = self.nutriantGroup.get(nutriantId, None)
           if value is None:
               self.nutriantGroup[nutriantId] = FoodNutrientDefault(nutriantName, group, unit)
           elif value.group != group or value.unit != unit:
             return False;
           return True;
 
       def printDetails(self, space=0):
           for id, fnd  in self.nutriantGroup.items():
              print space*' ', "nid:", id, "unit:", fnd.unit, "group:", fnd.group, "name:", fnd.nutriantName;

gFoodNutritionDefault = FoodNutrientGroup();

class FoodNutrient(object):
       def __init__(self , jNutriant):
           global gFoodNutritionDefault;
           self.nutrientId = int(jNutriant['nutrient_id'])
           self.group = jNutriant['group'].encode('utf-8').strip()
           self.unit = jNutriant['unit'].encode('utf-8').strip()
           nutrientName = jNutriant['name'].encode('utf-8').strip()

           #add default Nutrient Groups
           self.default = False;
           if gFoodNutritionDefault.isDefault(self.nutrientId, nutrientName, self.group, self.unit):
                self.default = True; 
 
           #TODO, add default nutrition m group and unit 
           self.values = list();
           self.values.append(float(jNutriant['value']));

           #print measure.printDetails(4)   
           for k in jNutriant['measures']:
              if  k is not None:
                 self.values.append(float(k['value']));

       def isZeroNutriant(self):
           value = self.values[0]; 
           if value == 0.0 or value == 0:
             return True;
           return False; 

       def isValidNutrition(self, measuresCount):
           if  len(self.values) != measuresCount:
               print 'food value count != measure count TODO add more logs'
               return sys.exit(-1);
               
           return not self.isZeroNutriant();

       def printDetails(self, space=0):
           #print space*' ', self.nutrientId, ":[", ','.join(map(str, self.values)), "]"
           if self.default == False: 
              print space*' ', "nid: ", self.nutrientId, " unit: ", self.unit, " group: ", self.group, "values: ", ','.join(map(str, self.values));
           else:
              print "[\"id\":", self.nutrientId, "\"v\":", "[", ','.join(map(str, self.values)), "]]";


class Food(object):
       def __init__(self , jFood, foodType):
         jNutriants  = jFood['nutrients'];  
         self.foodGroup = jFood['fg'].encode('utf-8').strip();
         self.foodName = jFood['name'].encode('utf-8').strip();

         #add all measures
         self.measures = list(); #list of FoodMeasure for this food
         measure =  FoodMeasure(foodType, 100, 1); #default measure
         self.measures.append(measure) 
         jFirstN =  jNutriants[0];
         #add all measures
         for k in jFirstN['measures']:
             if  k is not None:
                measure =  FoodMeasure(k['label'], k['eqv'], k['qty']);
                self.measures.append(measure)

         #go through nutrition 
         self.nutritions = list(); #list of FoodNutrient for this food
         for nutrition in jNutriants:
             nutriant = FoodNutrient(nutrition);
             if True == nutriant.isValidNutrition(len(self.measures)):
                self.nutritions.append(nutriant);

             #nutriant.printDetails(0)
       def printDetails(self, space):
           print space*' ', "name: ", self.foodName, " food group: ", self.foodGroup 
           for measure in self.measures:
               measure.printDetails(space)
           for nutrition in self.nutritions:
              nutrition.printDetails(space);


#contains map<id, Food>
class FoodDetails(object):
       def __init__(self):
            self.foodName=dict(); #map<id, Food>
            
       def add(self, jFood, foodType):
           ndbno = int(jFood['ndbno']);
           fd = Food(jFood, foodType);
           self.foodName[int(ndbno)] = fd;

       def getFoodDetails(self, filename):
           data_file=open(filename)
           data = json.load(data_file)
           f_report=data['report'];
           jFood = f_report['food'];
           self.add(jFood, f_report['type']); 


       def getAllFoodDetails(self, path):
           dirs = os.listdir( path )
           for file in dirs:
              food = path + "/" + file
              #print "Reading " + food
              self.getFoodDetails(food);
         
       def getFoodNutritionDefault(self):
           #print default food nutrition details
           global gFoodNutritionDefault;
           return gFoodNutritionDefault;

       def getUniqueLabels(self):
           #print default food nutrition details
           global uniqueLabels;
           return uniqueLabels;

       def printDetails(self):
           #print default food nutrition details
           #global gFoodNutritionDefault;
           #gFoodNutritionDefault.printDetails();
           for id, food  in self.foodName.items():
              print "id: ", id;
              food.printDetails(4);

       def printFood(self, id):
           food = self.foodName.get(id); 
           print "id: ",  id;
           food.printDetails(4);


