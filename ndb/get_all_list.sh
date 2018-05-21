#!/bin/bash

source api_key.sh
unset LD_LIBRARY_PATH
mkdir -p list

#get All food
./list.sh f
#get All nutrition
./list.sh n
#get all food groups
./list.sh g

#get all speciality nutrition
./list.sh ns

#get all standard release nutrition
./list.sh nr

