from pwn import *

print(cyclic(50))  # The DeBraun cyclic pattern. It is important to find offsets for buffer overflows. We can call
# it directly using pwn

print(cyclic_find("laaa"))  # We can also find the cyclic pattern of a string using cyclic_find

print(shellcraft.sh())  # We can directly work with assembly using this command
print(hexdump(asm(shellcraft.sh())))  # We can have the hexdump of the shellcode(assembly) in asm using this command

# p = process("/bin/sh")  # We can start a process using this command
# p.sendline("echo Hello, friend!;")  # We can send this line to our started process
# p.interactive()  # We can make the process we started be interactive using this command

# r = remote("127.0.0.1", 1234)  # We can also start a process on a remote workstation
# r.sendline("Hello, friend!")  # We can send a line on their shell using this command
# r.interactive()  # We can start an interactive session for the remote machine
# r.close()   # We can close the interactive session using this command

print(p32(0x13371337))  # We can pack data using this command. The numbers can effectively change though
print(hex(u32(p32(0x13371337))))  # We can unpack the data in the above line using this process. We specifically
# ask to print it in hex because the input in the above line was in hex

l = ELF('/bin/bash')  # We can load files this way using pwntools. ELF stands for Executable and Linkable Format
print(hex(l.address))  # We can look at the hex address of our program using this command
print(hex(l.entry))  # We can also see the entry point of the program

print(hex(l.got['write']))  # We can know the address of a specific symbol from the global offset table
print(hex(l.plt['write']))  # We can also grab information about a specific sample from the procedure linkage table

for address in l.search(b'/bin/sh\x00'):  # We are searching for addresses where we can find the /bin/sh stream
    # with a null terminator
    print(hex(address))

print(hex(next(l.search(asm('jmp esp')))))  # We can search for a specific address in the ELF which isn't represented
# as a stream

r = ROP(l)  # The ROP function makes it much easier on us to find this streams and addresses
print(r.rbx)  # This lets us search for specific gadgets in the ELF. This time, we're searching for rbx.

print(xor("A", "B"))  # We have access to hashing, encryption and encoding functions with pwntools. XOR is one of them.
print(xor(xor("A", "B"), "A"))  # We can make sure of the above result this way

print(b64e(b"test"))  # We have access to base64 encoding in pwntools.
print(b64d(b"dGVzdA=="))  # We have access to base64 decoding as well.

print(md5sumhex(b"hello"))  # We also have md5 sums

print(sha1sumhex(b"hello"))  # We have access to sha1 as well. Use this with hex as it will be confusing otherwise.

print(bits(b'a'))   # We can print the bits for characters and strings
print(unbits([0, 1, 1, 0, 0, 0, 0, 1]))  # We can change bits to their corresponding characters or strings.

