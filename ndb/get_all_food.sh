#!/bin/bash

source api_key.sh
unset LD_LIBRARY_PATH
mkdir -p food

> ./tmp.txt
for filename in list/list_f_*; do
    echo $filename
    sed -n '/\"id\": \"/p' $filename | cut -d'"' -f4 >> ./tmp.txt
done

filename=./tmp.txt
while read -r line
do
    echo "$line"
    ./food.sh $line
    sleep 5
done < "$filename"

exit 0

