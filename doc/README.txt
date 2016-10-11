https://bitbucket.org - sit****@g**/Koo


Note:: www.php.test.com is local site and this need to be replaced with www.mobileserf.com/ctg/foodtogo for actual testing.
  All request is in the form {"cmd": "command name" , "id"=1, "data": { data specific to query }}

REPLACE some string under data directory
=======================================
curl -H "Content-Type: application/json" -X POST -d '{"dir": "food", "from": "nutrition_list", "to": "nutrition_list"}' http://www.mobileserf.com/ctg/foodtogo/exec.php
 
Get Nutrition
=============
curl -H "Content-Type: application/json" -X POST -d '{"cmd": {"name": "nutrition","id": 10}, "data": {"id": 3	} }' http://www.php.test.com/index.php
curl -H "Content-Type: application/json" -X POST -d '{"cmd": {"name": "nutrition","id": 10}, "data": {"id": 1	} }' http://www.mobileserf.com/ctg/foodtogo/index.php

get food
==========
curl -H "Content-Type: application/json" -X POST -d '{"cmd": {"name": "food","id": 3}, "data": {"id": 1	} }' http://www.mobileserf.com/ctg/foodtogo/index.php

get store info - initial first request or whwnever user condition changes
=======================
//curl -H "Content-Type: application/json" -X POST -d '{"cmd": {"name": "stores","id": 1}, "data": {  "query": 
curl -H "Content-Type: application/json" -X POST -d '{"cmd": "stores", "data": {  "id": 1, "query": 
                 {
                        "userId": 12345,
			"last_date": 34325455656,
                        "location": {
                           "lat": 38.851130,
                           "lon": -77.344834
                        },
                        "filter": {
                                "max_stores": 20,
                        	"cusine": "italian",
                       	 	"serves": "all",
                        	"time": 18
                        }
                }
} }' http://www.mobileserf.com/ctg/foodtogo/index.php

//curl -H "Content-Type: application/json" -X POST -d '{"cmd": {"name": "stores","id": 1}, "data": {  "query": 
curl -H "Content-Type: application/json" -X POST -d '{"cmd": "stores", "data": {  "id": 1, "query": 
                {
			"userId": 12345,
			"last_date": 34325455656,
			"location": {
				"lat": 38.851140,
				"lon": -77.344814
			},
			"filter": {
                                "max_stores": 20,
				"cusine": "italian",
				"serves": "all",
				"time": 18
			},
			"transparent": {
				"id": 33434,
				"page": 10,
				"location": {
					"lat": 38.851130,
					"lon": -77.344834
				}
			}
		}
} }' http://www.mobileserf.com/ctg/foodtogo/index.php


Review:
=======
  can only write if you buy using the app
//rotten tomatto for less star 
/send a review
==============
curl -H "Content-Type: application/json" -X POST -d '{"cmd": {"name": "review","id": 4}, "data": {  "post": 
                {
			"userId": 12345,
			"last_date": 34325455656, /* last time a message send */
			"location": { /* current location */
				"lat": 38.851140,
				"lon": -77.344814
			},
                        "type": "food",
                        "item_id": 203,
			"rating": 5, /* star level */
                        "subject": "Very good food",
			"comment": "Hello. Please give our thanks to the Manager(s) and others for the wonderful room and bottle of sparkling wine for our Anniversary stay."
                        "parent_review_id": 123 /*only present if it is a review about previous review */

		}
} }' http://www.mobileserf.com/ctg/foodtogo/post.php

write a review about a review
=============================
   --same as above but use "parent_review_id": 123 json filed in the above request

like/useful a review
==============
curl -H "Content-Type: application/json" -X POST -d '{"cmd": {"name": "review_useful","id": 5}, "data": {  "post": 
                {
			"userId": 12345,
			"last_date": 34325455656, /* last time a message send */
			"location": { /* location*/
				"lat": 38.851140,
				"lon": -77.344814
			},
                        "type": "food",
                        "item_id": 203,
			"useful": "yes" /* this is either yes or no */

		}
} }' http://www.mobileserf.com/ctg/foodtogo/post.php

curl -H "Content-Type: application/json" -X POST -d '{"cmd": {"name": "reviews","id": 6}, "data": {  "request_id": 12345, "get": 
                {
			"userId": 12345,
			"last_date": 34325455656, /* last time a message send */
			"location": { /* last location */
				"lat": 38.851140,
				"lon": -77.344814
			},
                        "type": "food",
                        "item_id": 203,
                        "next_id": 0,
                        "max_count": 10

		}
} }' http://www.mobileserf.com/ctg/foodtogo/get.php

====
curl http://www.php.test.com/img.php?file=resource/food/burger.jpg
img.php?file=resource/food/burger.jpg
