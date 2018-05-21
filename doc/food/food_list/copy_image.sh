#!/bin/bash

for FILE in `ls -d *` 
do
    if test -d $FILE
    then
      echo "$FILE is a subdirectory..."
    fi
done
