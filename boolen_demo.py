valid = True
not_valid = False

print(valid)
print(not_valid)

print(valid == True)  # This is not an assignment statement, it's verifying if the variable is true or not
print(not_valid == True)

print(valid != True)  # This is the opposite of ==. It verifies if the variable is the opposite of the given boolean
# value
print(not_valid != True)  # != stands for not equal to

print(not valid)  # This is another way to verify if the variable has a True or False value
print(not not_valid)

print((10 < 9) == True)  # This is another thing we can check if it is true
print((10 == 10) == True)
print((10 != 10) == True)
print((10 >= 10) == True)
print((10 <= 10) == True)
print((10 > 9) == True)

print("--------")

print((10 < 9))  # We don't necessarily need the true boolean sign to get the results
print((10 == 10))
print((10 != 10))
print((10 >= 10))
print((10 <= 10))
print((10 > 9))

print("-------")

print(10 > 5 and 10 < 5)  # We can compare two or more statements using operators in Python.
print(10 > 5 or 10 < 5)

print(bool(0))  # Boolean of 0 represents False
print(bool(1))  # Boolean of 0 represents True

print(10 + 10)  # You can use Python to perform arithmetic calculations.
print(10 - 10)
print(10 / 10)
print(10 // 10)  # The // sign represents floor division

print(10 / 3)
print(10 // 3)
print(10 % 3)

print(10 * 10)
print(10 ** 10)  # ** stands for "the power of"
print(10 % 10)

x = 10
print(x)
x = x + 1
print(x)
x += 1  # This is the short form version of x = x + 1
print(x)
x -= 1
print(x)
x *= 5
print(x)
x /= 5
print(x)

x = 13
print(bin(x))  # Binary representation of x
print(bin(x)[2:].rjust(4, "0"))  # This cancels the 0b part out of the binary representation. We will learn why later.
# I'm gonna play with it by myself

y = 5
print(bin(y)[2:].rjust(4, "0"))

print(bin(x | y)[2:].rjust(4, "0"))  # This analyzes the binaries bit by bit and shows whether the final is 0 or 1.
# The results depend based on the fact that the operation is or(|) or and(&)
# | is a bitwise or and & is a bitwise and
print(x & y)

print(bin(x >> 1)[2:].rjust(4, "0"))  # x >> 1 means perform a bitwise shift of one. It means we moved all the bits
# across one space. An extra 0 we're seeing is because of the right justification

print(bin(x << 1)[2:].rjust(4, "0"))  # You can do a bitwise shit in another direction as well.
