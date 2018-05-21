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
curl -H "Content-Type: application/json" -X POST -d '{"cmd": {"name": "reviews","id": 6},
           "data": {  "request_id": 12345,
               "post":
                {
                        "userId": 12345,
                        "last_date": 34325455656,
                        "location": { 
                                "lat": 38.851140,
                                "lon": -77.344814
                        },
                        "type": "food",
                        "item_id": 203,
                        "store_id": 1, 
                        "rating": 5, 
                        "subject": "Very good food",
                        "description": "Hello. Please give our thanks to the Manager(s) and others for the wonderful room and bottle of sparkling wine for our Anniversary stay.",
                        "parent_review_id": 123,
                        "name": "Omar", 
                        "date": 1478687908

                }
} }' http://www.mobileserf.com/ctg/foodtogo/post.php 

http://www.php.test.com/post.php

curl -H "Content-Type: application/json" -X POST -d '{"cmd": {"name": "like","id": 7},
           "data": {  "request_id": 12345,  
               "post":
                {
                        "userId": 12345,
                        "last_date": 34325455656, 
                        "location": { 
                                "lat": 38.851140,
                                "lon": -77.344814
                        },
                        "type": "food", 
                        "item_id": 203, 
                        "store_id": 1, 
                        "date": 1478687908,
                        "sub_type": { 
                           "name": "review",
                           "id": 54321
                        },
                        "like": true 

                }
} }' http://www.php.test.com/post.php

curl -H "Content-Type: application/json" -X POST -d '{
	"cmd": {
		"name": "like",
		"id": 7
	},
	"data": {
		"request_id": 12345,
		"post": {
			"userId": 12345,
			"last_date": 34325455656,
			"location": {
				"lat": 38.851140,
				"lon": -77.344814
			},
			"type": "food",
			"item_id": 203,
			"store_id": 1,
			"date": 1478687908,
			"sub_type": {
				"name": "review",
				"id": 54321
			},
			"like ": true
		}
	}
}' http://www.php.test.com/post.php

http://www.mobileserf.com/ctg/foodtogo/get.php

//food group
============
curl -H "Content-Type: application/json" -X POST -d '{"cmd": {"name": "food_group","id": 53},
           "data": {  "request_id": 12345,
           "get": {
                        "test": false,
                        "userId": 12345,
                        "last_date": 34325455656,
                        "location": {
                                "lat": 38.851140,
                                "lon": -77.344814
                        }
                }
} }' http://www.mobileserf.com/ctg/foodtogo/get.php
