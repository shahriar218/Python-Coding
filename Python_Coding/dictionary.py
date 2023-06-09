my_dictionary = {"1":"apple", "2":"ball", "year": 1992, "bool": False}
print(my_dictionary)
print(my_dictionary['year'])
print(my_dictionary['2'])

my_dict = {"color":["red","green","yellow","black"], "brand":"ford", "year": 1992}
print(my_dict)

dictionary = dict(name="John", age=54, country="Sweden")
print(dictionary)

# find keys
x = dictionary.keys()
print(x)

# find values
y = dictionary.values()
print(y)
print(type(y)) # data-type dict_values
print(list(y)) # data-type list

dictionary["height"] = 6.3 # add new key-value to dictionary
print(dictionary)

print(y) # check values after add new value

print(dictionary.items())

print(dictionary)

dictionary["passport"] = 123459800
print(dictionary)