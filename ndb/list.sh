#!/bin/bash

source api_key.sh
unset LD_LIBRARY_PATH
mkdir -p list

#get food
LT="$1"
MAX=500
OFFSET=0
while true
do
  FILE_NAME="list/list_$LT"_$OFFSET
  PARAMETER="{\"api_key\":\"$API_KEY\", \"lt\":\"$LT\",\"max\":\"$MAX\",\"sort\":\"id\", \"offset\":\"$OFFSET\"}"
  QUERY="-o $FILE_NAME -H \"Content-Type:application/json\" -d '$PARAMETER' $API_KEY@api.nal.usda.gov/ndb/list"
  echo "curl $QUERY"
  test=$(curl -o $FILE_NAME -H "Content-Type:application/json" -d "$PARAMETER" $API_KEY@api.nal.usda.gov/ndb/list)
  #execute query
  #`$QUERY`

  #./parse_list.py $FILE_NAME
  total=`./get_total.py $FILE_NAME`
  echo $total
  if [[ $total < $MAX ]] ; then
        exit 0;
  else
     sleep 4
  fi
  OFFSET=$((OFFSET + 500))    
  echo $OFFSET
done
