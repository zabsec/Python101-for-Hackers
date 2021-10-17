add_4 = lambda x: x + 4  # This is an example of a lambda function
print(add_4(4))  # This argument is inserted into the variable found in the lambda function

add = lambda x, y: x + y  # We can have two or more paramters in lambda as well
print(add(10, 4))


def addf(x, y):  # This is equivalent to the "add" lambda function
    return x + y


print(addf(10, 4))

print((lambda x, y: x + y)(10, 4))  # We can create, evaluate and print a lambda function all in one line.

is_even = lambda x: x % 2 == 0  # We can easily see if a number is even or odd using lambda functions. This is useful
# for hacking scripts
print(is_even(2))
print(is_even(3))

blocks = lambda x, y: [x[i:i + y] for i in range(0, len(x), y)]  # We can use lambdas to iterate. I need to further
# inspect this statement
print(blocks("string", 2))

to_ord = lambda x: [ord(i) for i in x]  # This can help put the elements in order for strings
print(to_ord("ABCD"))


def to_ord2(x): # This is just the "to_ord" lambda written in a normal function.
    ret = []
    for i in x:
        ret.append(ord(i))
    return ret


print(to_ord2("ABCD"))

