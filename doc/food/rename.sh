#!/bin/bash

i=1
for FILE in `ls -k image_tmp/*.jpg` 
do
    if test -f $FILE
    then
      fname=$(basename $FILE)
      mv $FILE   image_tmp/$i.jpg   
      echo "image_tmp/$i.jpg a file..."
      ((i++))  
    fi
done
