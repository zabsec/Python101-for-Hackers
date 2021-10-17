set1 = {"a", "b", "c"}
print(set1)  # When it's printed, the elements of the set are printed randomly
print(type(set1))

set2 = {"a", "a", "a"}  # duplicate values are counted as only one value
print(set2)
print(len(set2))

set3 = {"a", 0, True}  # We can have different data types as elements of sets
print(set3)

set4 = set(("b", 1, False))  # This is another way of declaring a set
print(set4)

set1.add("d")  # We can add an element to a set
print(set1)

set3.update(set4)  # This combines the elements
print(set3)

list1 = ["a", "b", "c"]
set4 = {4, 5, 6}
print(set4)

set4.update(list1)  # We can combine lists with sets
print(set4)

set5 = {4, 5, 6}
set6 = set4.union(set5)  # This is another way to combine sets

set4.remove(4)  # We can remove an element from sets using the remove function
print(set4)

set4.discard(4)  # This won't bring up an error even if the element is not there but will remove it if it is in the set
print(set4)

print(set1)
set1.pop()  # This will pop a random element since sets are not ordered.
print(set1)