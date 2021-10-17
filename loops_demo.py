a = 1
print(a)
a += 1
print(a)
a += 1  # This increases the value of the variable again and again
print(a)

a = 1
while a < 5:  # This condition goes on until the exit condition is met. This is called a while loop.
    a += 1
    print(a)

for i in [0, 1, 2, 3, 4]:  # This is called a for loop.
    print(i + 6)  # This prints each element by adding 6 to it.

print("----")  # This is a delimiter to keep track of the lesson
for i in range(5):  # The range function means it starts from 0 but stops right before it reaches 5.
    print(i + 6)

for i in range(3):
    for j in range(3):  # This is called a nested loop.
        print(i, j)

print("----")

for i in range(5):
    if i == 2:
        break  # This breaks the loop which means it can stop the loop before it finishes.
    print(i)

print("----")

for i in range(5):
    if i == 2:
        continue  # This will skip the given condition then goes back to the start of the loop and reiterates the
        # loop and continue iterating
    print(i)

print('----')

for i in range(5):
    if i == 2:
        pass    # Similar to the continue statement but it does not reiterrate anything, it just passes the condition
        # and lets the loop finish.
    print(i)

    for c in "string":
        print(c)    # We can iterate over each individual string

    for key, value in {"A": 1, "B": 2, "C": 3}.items():
        print(key, value)   # We can iterate over each item in a dictionary





