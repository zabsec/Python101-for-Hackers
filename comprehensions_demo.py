list1 = ['a', 'b', 'c']  # This is a normal list. From this we can create a list comprehension.
print(list1)

list2 = [x for x in list1]  # It iterates over each element in list1 and adds it into list 2. This is called a
# comprehension.
print(list2)

list3 = [x for x in list1 if x == 'a']  # We can add conditionals in list comprehensions
print(list3)

list4 = [x for x in range(5)]  # This takes the range from 0-4 then iterates it on this list.
print(list4)

list5 = [hex(x) for x in range(5)]  # This turns each element in the range(5) to hex when it iterates it into list5
print(list5)

list6 = [hex(x) if x > 0 else "X" for x in range(5)]  # Another way to give complicated conditionals in comprehensions.
print(list6)

list7 = [x * x for x in range(5)]  # For each element in each range(5), we can perform arithmetic operations before
# they are iterated into our list
print(list7)

list8 = [x for x in range(5) if x == 0 or x == 1]  # We can use booleans in list comprehensions
print(list8)

list9 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # This is a nested list

list10 = [y for x in list9 for y in x]  # This is saying "take the lists of elements y from the nested list x and
# create a new list of each y that are in x"
print(list10)

set1 = {x + x for x in range(5)}  # This is a set comprehension
print(set1)

list11 = [c for c in "string"]  # We can make list comprehensions from strings
print(list11)

print("".join(list11))  # This turns the list back into one string since there are no spaces in there.

print("-".join(list11))  # This turns into a string with a hyphen between each letter.
