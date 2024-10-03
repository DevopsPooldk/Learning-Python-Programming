# Persnal info :
personal_info={
"name" : "Dinesh",
"age" : 20,
"Profation": "Devops",
"Year" :{
    "sem": 5,
    "year": 2,
}
}
print(personal_info["Year"]["sem"])

print(list(personal_info.keys())) # return all keys

print(list(personal_info.values())) #return all values

print(list(personal_info.items())) #Returns all (key,value) pairs as tuples. Value return with tuples

print(personal_info.get("name")) # a key geting rong .get function print None value.

# We create new dictionary and update it with old dictionary.

new_Dict= { 
    "City" : "Beed",
    "Hobie" :"Business",

}
personal_info.update(new_Dict) # update method
print(list(personal_info))
