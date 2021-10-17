print(1)
print(2)  # If we put a spcae at the start, This will cause an indentation error

try:
    f = open("addasdsda")
except:
    print("File does not exist!")  # This will be the output for all errors, which is not advisable.

try:
    frehurie  # This is random string that will cause an error
    f = open("asdasdasdsa")
except FileNotFoundError:  # We can make exceptions for different error types
    print("The file does not exist!")
except Exception as e:
    print(e)  # This prints what exception it is.
finally:  # This message will be displayed regardless if an exception is caught or not.
    print("this message!")

n = 100
if n == 0:
    raise Exception("n can't be 0!")  # We can raise exceptions using this syntax
    # if n is a string, this exception won't be reached and Python will raise an
    # unsupported operand type error
if type(n) is not int:
    raise Exception("n must be an int!")    # This exception will handle the unsupported operand type error.

print(1 / n)

n = 0
assert(n != 0)  # This is another way to handle errors or make rules. Breaking this rule will cause an assertion error.
print(1/n)

