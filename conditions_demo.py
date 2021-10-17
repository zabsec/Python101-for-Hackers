if True:
    print("Hello, friend")

if False:  # There is nothing that's false so this condition won't execute.
    print("It's dangerous")

if not False:
    print("Hello again, friend")

if 1 < 1:  # This is another example of a condition that won't execute and therefore, the code inside it is unreachable
    print("1 < 1")
elif 1 <= 1:  # elif/ else-if is a way of giving another condition to execute in case the other statements are not
    # reachable
    print("1 <= 1")
else:  # This condition executes if the if and elif statements are not executed or the condition does not fit.
    print("else 1")

if 1 < 1:
    print("1 < 1")
elif 1 <= 1:  # Because this condition is true and comes first this is printed.
    print("1 <= 1")
elif 2 <= 2:  # Despite the fact that the condition is true, it won't be executed as the first elif statement is
    # executed first
    print("2 <= 2")
else:
    print("else reached")

if 1 > 0 and 0 < 1:  # Since both are true, this executes
    print("1 > 0 and 0 < 1")

if 1 < 0 and 0 > 1:  # Since this statement equates to false, this statement won't print
    print("1 < 0 and 0 > 1")

if 1 < 0 or 0 < 1:  # In an or statement, if one of them is true, the statement is printed and the code is reachable
    print("1 < 0 or 0 < 1")

if (1 < 0 or 0 < 1) and 1 == 1:  # This is us just playing with operators. As long as the last calculation is true,
    # the statement executes
    print("1 < 0 or 0 < 1")

if (1 < 0 or 0 < 1) or 1 == 0:
    print("1 < 0 or 0 < 1")

if 0 < 1: print("0 < 1")    # This is a shorthand

print("1 >= 1") if 1 >= 1 else print("1 < 1")   # This is a ternary operator in use. The else statement must be there.
if 1 >= 1:  # This is just another way to write our ternary statement
    print("1 >= 1")
else:
    print("1 < 1")

if 0 > 1:
    print("1")
elif 0 < 1:
    print("2")
else:
    print("3")
print("1") if 0 > 1 else print("2") if 0 < 1 else print("3")    # This is the same operation as the one above.


