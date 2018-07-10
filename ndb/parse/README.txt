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


javascript 
==========
map to json => localStorage.myMap = JSON.stringify(Array.from(map.entries()));
json to map => map = new Map(JSON.parse(localStorage.myMap));


function mapToJson(map) {
    return JSON.stringify([...map]);
}
function jsonToMap(jsonStr) {
    return new Map(JSON.parse(jsonStr));
}

    
 fodd will be stored as <id, {array of labels, arrayof array of items} >

 e.g 


[
	[
		45000027, {
			"l": ["full", "Cup (64g)"],
			"g": [100, 64],
			"208": [55.0, 35.0],
			"209": [55.0, 35.0]
		}
	]
]


Sample run following in node
===========================
function mapToJson(map) {
    return JSON.stringify([...map]);
}
function jsonToMap(jsonStr) {
    return new Map(JSON.parse(jsonStr));
}

let mynutr = '[ [45000027, {"l": ["full", "Cup (64g)"], "g": [100, 64], "208": [55.0, 35.0], "209": [55.0, 35.0]}], [45000028, {"l": ["full", "Cup (64g)"], "g": [100, 64], "208": [55.0, 35.0], "209": [55.0, 35.0]}] ]'


//console.log(jsonToMap(mynutr))
let  mymap = jsonToMap(mynutr);
//console.log(mymap.get(45000027))
let myfood = mymap.get(45000028)
console.log(myfood["208"][0])
console.log(myfood["210"])


