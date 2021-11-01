from pwn import *
import sys

if len(sys.argv) != 2:  # This condition says that we expect two arguments in our Python program, with one being the
    # program name itself
    print("Invalid arguments!")
    print(">> {} <sha256 sum>".format((sys.argv[0])))
    exit()

wanted_hash = sys.argv[1]  # This is the second CLI argument which would be the 256 hash for the user
password_file = "rockyou.txt"  # This is going to be our password file
attempts = 0  # This is how we'll keep track of our attempts

with log.progress('Attempting to crack: {}!\n'.format(wanted_hash)) as p:  # log.progress is a pwn module item that
    # shows the progress of our hacking
    with open(password_file, "r", encoding='latin-1') as password_list:  # We encode the file because rockyou has some
        # passwords that need to be formatted/encoded properly
        for password in password_list:
            password = password.strip("\n").encode('latin-1')
            password_hash = sha256sumhex(password)  # We need this to hash each password to match with the
            # wanted_hash. The hash needs to be in hex format
            p.status("[{}] {} == {}".format(attempts, password.decode('latin-1'), password_hash))   # This shows us
            # the number of attempts, and what password it's trying, along with what the hash of the password is
            if password_hash == wanted_hash:
                p.success(
                    "Pasword hash found after {} attempts! hashes to {}!".format(attempts, password.decode('latin-1')))
                exit()
            attempts += 1   # if the password hash is not found at this point, an attempt is added up to the tally.
        p.failure("Password hash not found")

