import json

userJson = '{"first_name":"Farhan","last_name":"Rozzi","age":19}'

# json to dictionary

jsonString = json.loads(userJson)
print(jsonString)
print(jsonString['first_name'])

car = {"name": "Ford", "model": "Mustang", "year": 1970}
toJson = json.dumps(car)

print(toJson)