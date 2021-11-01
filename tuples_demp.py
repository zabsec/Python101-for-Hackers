tuple_items = ("item1", "item2", "item3")  # We declare tuples this way
print(tuple_items)
print(type(tuple_items))

tuple_numbers = (1, 2, 3)
print(tuple_numbers)
print(type(tuple_numbers))

tuple_repeat = ('Combine!',) * 4  # We can also write tuples this way
print(tuple_repeat)
print(type(tuple_repeat))

tuple_mixed = ("A", 1, ("A", 1))  # A tuple can have different types of items in it including a nested tuple
print(tuple_mixed)
print(type(tuple_mixed))

tuple_combined = tuple_items + tuple_numbers
print(tuple_combined)
print(type(tuple_combined))

item1, item2, item3 = tuple_items  # This is a way we can unpack tuples
print(item1)
print(item2)
print(item3)

print("item2" in tuple_items)  # Check if a string or any item is in a tuple
print("item4" in tuple_items)

print(tuple_items.index("item2"))  # Gives us the index number of an item. Will give us -1 if it doesn't exist

print(tuple_items[0])  # Prints the item that is in the indicated index number of the tuple

print(len(tuple_items))  # Prints the length of a tuple

print(tuple_items[-1])  # This is the last item that's getting printed. negative numbers means counting backwards

print(tuple_items[0:2])  # We can print parts of the tuple using these index numbers. The last index number won't be
# included in the print.
print(tuple_items[:2])  # Same concept with the index number starting from 0
print(tuple_items[-3:-1])   # We can count the index numbers backwards

string1 = "I am a string!"
print(string1[0:4]) # The concept of indexes also applies with strings
print(string1[:-1])
