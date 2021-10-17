list1 = ["A", "B", "C", "D", "E", "F"]  # This is how we can declare a list
print(list1)

list2 = ["A", 1, 2.0, ["A"], [], list(), ("A"), False]  # A list can contain different data types including a nested
# list
print(list2)
print(type(list2))

print(list1[0])  # We can use indexing to print specific elements of the list
print(list1[-1])
print(list2[3][0])  # Here we are asking to get into the nested list on the 3rd index then print the first element in
# that list
print(list2[3][-1])  # We can do the same thing while counting backwards

list1[0] = "X"  # We can change contents of the list using this syntax
print(list1)

del list1[0]  # We can also delete contents of the list using this syntax
print(list1)

list1.insert(0, "A")  # We can insert an element by first showing the index number we want it on and then inserting
# the element
print(list1)

del list1[0]
print(list1)

list1 = ["A"] + list1  # This is another way we can insert elements. This adds it to the front of the list
print(list1)

list1.append("G")  # Another way to insert elements. This adds it on the last position of the list.
print(list1)

print(max(list1))  # It will let us know the maximum value in the list.
print(min(list1))  # It will let us know the minimum value in the list.

print(list1.index("C"))  # We can find out the index of an element using this syntax. Python will return -1 if the
# element is not found in the list.
print(list1[list1.index("C")])  # This is a nested expression where list1 gets the index of an element as an input,
# then it will spit out the element in return.

list1.reverse()  # Reverses the order of the whole list
print(list1)

list1 = list1[::-1]  # This is another way to reverse the list
print(list1)

print(list1.count("A"))  # This counts the number of times the element in the input appears in the list
list1.append("A")
print(list1)
print(list1.count("A"))

list1.pop()  # This removes the last element of the list
print(list1)

list3 = ["H", "I", "J"]
print(list3)

list1.extend(list3)  # This adds the list in the input to the list the function is being used on.
print(list1)

list1.clear()   # This deletes every element in the list and it becomes an empty list
print(list1)

list4 = [8, 12, 5, 6, 17, 2]
print(list4)

list4.sort()    # We can sort the list in increasing order using the sort function
print(list4)

list4.sort(reverse=True)    # We can sort the list in decreasing order using the sort function
print(list4)

list5 = list4   # This is a reference to list4 and not an actual copy
print(list4)
print(list5)

list5[2] = "X"  # This will modify both list4 and list5
print(list5)
print(list4)

list6 = list4.copy()    # This is a legitimate copy of list4 and can be modified without modifying list4
print(list4)
print(list6)

list6[2] = "A"  # This only modifies list6 and not list4
print(list6)
print(list4)

list7 = ["1", "2", "3"]
print(list7)

list8 = list(map(float, list7)) # This would map each element of list7 and turn it into a float(as long as it's
# applicable)
print(list8)


