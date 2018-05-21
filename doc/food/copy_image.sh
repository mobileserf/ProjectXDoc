#!/bin/bash


for FILE in `ls -d food_list/*` 
do
    if test -d $FILE
    then
      fname=$(basename $FILE)
      ./parse_list.py $FILE/list_f_$fname $FILE "image_tmp"     
      echo "$fname is a subdirectory..."
      
    fi
done
