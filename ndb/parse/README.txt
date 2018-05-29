LD_LIBRARY_PATH=/home/ajose/repo/thirdparty/proto3/protobuf/src/.libs
PATH=/home/ajose/repo/thirdparty/proto3/protobuf/src/.libs:$PATH

protoc -I=. --python_out=. ./nutrition.proto



//TODO - manufacture & commerical name 
//TODO - measure label can be same but qty can be different

                       "measures": [
                        {
                            "label": "fl oz",
                            "eqv": 29.8,
                            "qty": 1.0,
                            "value": 51.0
                        },
                        {
                            "label": "fl oz",
                            "eqv": 357.0,
                            "qty": 12.0,
                            "value": 607.0
                        }
                    ]



../food/food_* , how to read
common-  ndb, food group 
      mesaures list - measures.label, mesaures.eqy, measures.qty
                       First one: Full (or food.type), 100, 1   
                               *: food.type(Default Full), 100, 1  
  
  nutrition list - id, group, unit (default is gram) 
                   [list of values that equal to size of "mesaures list"] 
