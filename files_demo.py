f = open('top-100.txt')
print(f)

f = open("top-100.txt", 'rt')  # The mode is reflected in the output.
print(f)

print(f.read())  # We can read the contents of the line this way'

print(f.readlines())  # This shows us the contents of the file in an array

print(f.readlines())  # On the second execution, readlines gives an empty array because the first has already read
# to the end of the array

f.seek(0)  # This will seek the 0th index number in the file, making it readable again by readlines
print(f.readlines())  # This will read the file properly

f.seek(0)
for line in f:
    print(line.strip())  # This will strip the file line by line. Useful for bruteforce attacks.

f.close()  # We can close the file once we're done with it.

f = open("test.txt", "w")  # We can create a file by using write mode
f.write("test line!")
f.close()

f = open("test.txt", "a")  # This is append mode. It will add to the file without removing what was in there.
f.write("test line two!")
f.close()

print(f.name)  # Once we've assigned a variable to a file, we can know the name using the name method
print(f.closed)  # We can check if the file is closed
print(f.mode)  # We can see the status of what mode the file was on before closing or what mode it's on while it's
# still open.

with open('rockyou.txt', encoding='latin-1') as f:  # We changed the encoding because rockyou has passwords not
    # encoded by utf-8
    for line in f:  # This is another way we can play with files.
        pass


