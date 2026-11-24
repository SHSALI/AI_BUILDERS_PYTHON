#Dictionary : ordered , changeable , do not allow duplicate 

my_dict= {
    "name" : "Sayed hussain Ali",
    "age" : "30"  ,
    "age" : "31"  
}

print(my_dict)
print(type(my_dict))
print(len(my_dict))

# Accessing items
print(my_dict["name"])
print(my_dict["age"])

new_dict= {
    "name" : "Sayed hussain Ali",
    "age" : "30"  ,
    "age" : "31"  ,
    "cars" : ["BMW" , "FORD" , "TOYOTA"]
}
print(new_dict)

my_dict["age"]="22"
print(my_dict)

my_dict.update({"name" : "Sayed hussain Ali", "age" : 31 , "city" : "Manama"})
print(my_dict)

my_dict.update({"city" : "AL_Dair"})
print(my_dict)

my_dict["city"]="Arad"
print(my_dict)

my_dict["country"]="Bahrain"
print(my_dict)

my_dict.pop("age")
print(my_dict)

del my_dict["city"]
print(my_dict)

my_dict.clear()
print(my_dict)