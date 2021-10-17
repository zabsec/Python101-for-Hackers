test = input()  # We can use this syntax to take in input from the user
print(test)

test = input("Enter the IP: ")  # We can ask questions to the user in the input form
print(test)

while True:
    test = input("Enter the IP: ")
    print(">>> {}".format(test))    # This is the format method we learned in a previous method
    if test == "exit":  # This is a condition that makes the loop stop when it is satisfied.
        break
    else:
        print("exploiting...")

