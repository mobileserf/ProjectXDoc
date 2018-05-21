#!/bin/bash

source api_key.sh
unset LD_LIBRARY_PATH
mkdir -p food

#curl -X GET 'http://api.nal.usda.gov/ndb/reports/?ndbno=01009&type=b&format=json&api_key=DEMO_KEY'
#get food
NDB_NO="$1"
TYPE="f"
  FILE_NAME="food/food_$NDB_NO"
  PARAMETER="http://api.nal.usda.gov/ndb/reports/?ndbno=$NDB_NO&type=f&format=json&api_key=$API_KEY"
  curl -X GET "$PARAMETER" > $FILE_NAME 
  #PARAMETER="{\"api_key\":\"$API_KEY\", \"ndbno\":\"$NDB_NO\",\"type\":\"$TYPE\"}"
  #QUERY="-o $FILE_NAME -H \"Content-Type:application/json\" -d '$PARAMETER' $API_KEY@api.nal.usda.gov/ndb/reports"
  #echo "curl $QUERY"
  #test=$(curl -o $FILE_NAME -H "Content-Type:application/json" -d "$PARAMETER" $API_KEY@api.nal.usda.gov/ndb/reports)
  #execute query
  #`$QUERY`

