#! /usr/bin/python

#import nutrition_pb2
import os, sys, glob
from pprint import pprint
import json

import parseList
import parseFood


#ndb path
gBasePath=".."

gFoodListDir=gBasePath + "/list"

#get all nutrition groups
print "Get All Nutrition Group:" 
gNtrGroup = parseList.ParseList();
gNtrGroupFile=gFoodListDir + "/list_n_group"
gNtrGroup.getList(gNtrGroupFile);
#gNtrGroup.printDetails();
#gNtrGroup.printJavaObj();

print "Get All Food Group:" 
gFoodGroup = parseList.ParseList();
gFoodGroupFile=gFoodListDir + "/list_g_0"
gFoodGroup.getList(gFoodGroupFile);
#gFoodGroup.printDetails();
#gFoodGroup.printJavaObj();


print "Get All Nutrition:" 
gNutritions = parseList.ParseList();
gNutritionsFile=gFoodListDir + "/list_n_0"
gNutritions.getList(gNutritionsFile);
#gNutritions.printDetails();
#gNutritions.printJavaObj();


print "Get All Foods:" 
gFoods = parseList.ParseList();
files = glob.glob(gFoodListDir+'/list_f_*')
for file in files:
    gFoods.getList(file);
#gFoods.printDetails();
#print gFoods.getSize();
#gFoods.printJavaObj();

gFoodDir=gBasePath + "/food"
foods = parseFood.FoodDetails();
foods.getAllFoodDetails(gFoodDir);

nutriants = foods.getFoodNutritionDefault();
nutriants.printDetails();

labels = foods.getUniqueLabels();
labels.printDetails();

foods.printDetails();
sys.exit(0)


#print  json.dumps(foods.__dict__);
# Main procedure:  Reads the entire address book from a file,
#   adds one person based on user input, then writes it back out to the same
#   file.
if len(sys.argv) != 1:
  print "Usage:", sys.argv[0] 
  sys.exit(-1)


print "hai"
