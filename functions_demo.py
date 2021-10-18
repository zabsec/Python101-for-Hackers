def function1():
    print("hello from functions!")


function1()  # The function executes only when we call it
function1()  # We can call functions as many times as we want


def function2():
    return "hello from function2!"  # This is returning a value, not printing it


print(function2())  # To see the return statement of a function, you have to print it, not just call it.
return_from_function2 = function2()  # This is another way to store the return statement in a variable
print(return_from_function2)  # This is another way we print the return statement of a function.


def function3(s):  # The s in here is called a parameter and it should be included when the function is called.
    print("\t{}".format(s))


function3("parameter")  # This parameter is not optional!


def function4(s1, s2):  # We can have more than one parameter in a function
    print("{} {}".format(s1, s2))


function4("Hello,", "Friend")  # We can print anything we want in here
function4(s2="Hello,", s1="Friend")  # We can determine which comes first when calling our function


def function5(s1="default"):  # We can assign default values to parameters
    print("{}".format(s1))


function5()  # We don't have to mention the argument of the function here since there is already a default value.
function5("Anything")  # We can always give it our own value even if it has a default value.


def function6(s1, *more):  # In this statement, we're saying there can be one or more(unknown number) arguments.
    print("{} {}".format(s1, " ".join([s for s in more])))  # We turn the contents of more into a list then join them
    # back to a string with a statement. Between each element of more there will be a space.


function6("function 6")  # We can use just one argument
function6("function 6", "says", "Hello,", "Friend")  # We can use as many arguments as we want


def function7(**ks):  # This means the function needs a dictionary of arguments
    for a in ks:
        print(a, ks[a])


function7(a="1", b="2", c="3")  # This will turn it into a dictionary.


def function8(s, f, i, l):  # We can have many arguments with a different .
    print(type(s))
    print(type(f))
    print(type(i))
    print(type(l))


function8("string", 1.0, 1, ['l', 'i', 's', 't'])

v = 100
print(v)


def function9():
    v = 5  # We can declare a local variable that works only in the function as well.
    print(v)  # A globally declared variable can be used inside a function. If there is a local variable and a
    # global variable with the same name, the local variable is used


function9()
print(v)


def function10():
    global v  # We're declaring that we're using the global v variable
    v += 1  # If we don't declare that we're using the global v, this isn't a declaration so this would cause an error


function10()


def function11():
    print("hello from function11")


def function12(s):
    print(s)


function12(function11())    # Functions can call another function


def function13(x):
    print(x)
    if x > 0:   # This condition has to be here because it won't stop.
        function13(x-1) # This is called recursion. It's recommended that you build recursion that actually stop.


function13(5)


def function14(x):
    while x >= 0:
        print(x)
        x -= 1


function14(5)

