#!/bin/bash

for FILE in `ls -d food_list/*` 
do
    if test -d $FILE
    then
      fname=$(basename $FILE)
      zip -r $FILE/$fname.zip $FILE/*     
      echo "$fname is a subdirectory..."
      
    fi
done
