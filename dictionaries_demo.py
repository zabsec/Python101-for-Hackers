dict1 = {"a": 1, "b": 2, "c": 3}  # This is how you declare a dictionary
print(dict1)
print(type(dict1))
print(len(dict1))

print(dict1["a"])  # We put the key instead of an index then Python will print out the value
print(dict1.get("a"))  # This is another way we can call a value by entering the key

print(dict1.keys())  # This prints all the keys in the dictionary
print(dict1.values())   # This prints all the values in the dictionary
print(dict1.items())    # This prints out all the dictionary in tuple form

dict1["a"] = 1  # We can't add duplicates. There will be no changes here.
print(dict1)

dict1["d"] = 4  # We can add the another key value pair in a dictionary
print(dict1)

dict1["a"] = 0  # We can change the value of a key using this method
print(dict1)

dict1.update({"a": 1})  # This is another way we can change
print(dict1)

dict1.pop("d")  # By entering the key here, it removes the key value pair from the dictionary.  By default,
# it removes the last key value pair of the dictionary if a key is not inserted in the input
print(dict1)

del dict1['c']  # This is another way we can delete a key value pair from the dictionary
print(dict1)

dict1['c'] = {"a": 1, "b": 2}   # We can create nested dictionaries. Values can be whole new dictionaries.
print(dict1)

dict2 = {}  # We can also create empty dictionaries
print(dict2)

dict3 = dict()  # This is another way we can create dictionaries
print(dict3)


