
proto dir - contains script for parsing food drom list and food directory

get All food list based on food , group and nutrition
  API home page = https://ndb.nal.usda.gov/ndb/doc/apilist/API-LIST.md
  usage ./getA-ll_list.sh

  files:  
    ./list.sh - get one of the list 
    ./get_total.py - get total number of list
    ./parse_list.py - parse the list  

Get All food based on above foodlist's ndbno
   ./get_all_food.sh
  files:
    ./food.sh <ndbno>
 



Food Group
========
message FGDetails {
   required string name = 1;
   repeated int32 foodId= 2;
};

message FoodGroup{
   required map<id, FGDetails> fgDetails= 1;
};

Nutrition Group
===============

message NutrientGroupId
{
   map <uint32, string> NutritionGId= 1;
};

message NGDetails {
   required string name = 1;
   repeated string  nGId = 2; /* NutrientGroupId */
};
message Nutritions {
   required map<id, NGDetails> = 1;
};

UnitMeasure
==========
message MeasureGroup {
  map<uint32, string > unit = 1;
};

Food List
========
message FoodName {
  string name = 1;
  string sd = 2; /* short description */
  uint32 foodGroup = 3;
};

message FoodList {
  map<uint32, FoodName> foodName = 1; 
};

Food
==========

message Food {
  map <int32, float > /* measureId, value */
};

message FoodDetails {
  map<uint32, Food> foodName = 1;

};
