curl -H "Content-Type: application/json" -X POST -d '{"cmd": {"name": "reviews","id": 6},
           "data": {  "request_id": 12345,
           "get": {
                        "userId": 12345,
                        "last_date": 34325455656, 
                        "location": { 
                                "lat": 38.851140,
                                "lon": -77.344814
                        },

                        "type": "food", 
                        "item_id": 203,
                        "store_id": 1, 
                        "transparent": 
                        {
                           "next_id": 0, 
                           "first_id": 0 
                        },
                        "max_count": 10 

                }
} }' http://www.php.test.com/get.php 

curl -H "Content-Type: application/json" -X POST -d '{"cmd": {"name": "reviews","id": 6},
           "data": {  "request_id": 12345,
           "get": {
                        "userId": 12345,
                        "last_date": 34325455656, 
                        "location": { 
                                "lat": 38.851140,
                                "lon": -77.344814
                        },

                        "type": "store", 
                        "item_id": 1,
                        "transparent": 
                        {
                           "next_id": 0, 
                           "first_id": 0 
                        },
                        "max_count": 10 

                }
} }' http://www.php.test.com/get.php


http://www.mobileserf.com/ctg/foodtogo/get.php

