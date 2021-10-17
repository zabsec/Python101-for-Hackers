import requests

x = requests.get('http://httpbin.org/get')

print(x.headers)  # This will show us the headers of the website. Headers are presented in a dictionary
print(x.headers['Server'])  # Since the header is presented in a dictionary format, we can pick a specific part of
# the header to display by entering the key
print(x.status_code)  # We can see the status code of the website using status_code

if x.status_code == 200:  # We can print different things based on the status code
    print("Success!")
elif x.status_code == 404:
    print("Not found!")

print(x.elapsed)  # This shows the time taken from the time the request is sent to the time it gets a response
print(x.cookies)  # This returns a cookie jar request

print(x.content)  # We can look at the content received. This is returned in bytes.
print(x.text)  # We can look at the the content received in human readable unicode format.

x = requests.get('http://httpbin.org/get', params={'id': '1'})  # We can add paraeters in our requests.
print(x.url)  # This displays the url, with any parameters that are added as well

x = requests.get('http://httpbin.org/get?id=2')  # We can specify the parameters directly with the link as well.
print(x.url)

x = requests.get('http://httpbin.org/', params={'id': '3'},
                 headers={'Accept': 'application/json', 'test_header': 'test'})  # We can add
# headers into our search parameter as well
print(x.text)

x = requests.delete('http://httpbin.org/delete')  # We can also use delete commands in the requests module
print(x.text)

x = requests.post('http://httpbin.org/post', data={'a': 'b', 'c': 'd', 'e': 'f'})  # We can use the post command
# and insert data using the requests module.
print(x.text)

files = {'file': open('google.png', 'rb')}
x = requests.post('http://httpbin.org/post', files=files)  # We can insert data this way in an HTTP post form
print(x.text)

x = requests.get('http://httpbin.org/get', auth=('username', 'password'))   # We can add authentication into a get
# form as well
print(x.text)

x = requests.get('https://expired.badssl.com', verify=False)  # We can also use the requests module to interact with
# https. To stop it from causing an error by saying the ssl is expired, we tell it not to verify the ssl
print(x.text)

x = requests.get('http://github.com', allow_redirects= False)    # We're telling it not to redirect us to anything.
print(x.headers)

x = requests.get('http://httpbin.org/get', timeout= 5)   # We can specify the amount of timeouts we allow.
print(x.content)

x = requests.get('http://httpbin.org/cookies', cookies = {'a': 'b'})    # This is called a stateful session as we are
# giving it session cookies that serve as credentials. Everything else we've been doing so far is a stateless request.
print(x.content)

x = requests.Session()  # We can use sessions as we don't have to update them every time unlike cookies. Using
# cookies for every request can be error prone and inefficient.
x.cookies.update({'a': 'b'})    # We can fill the cookie for the session this way.
print(x.get('http://httpbin.org/cookies').text) # Using this allows us to include the session in our request.
print(x.get('http://httpbin.org/cookies').text) # It will have the same result as it's a session and not just a cookie

x = requests.get('https://api.github.com/events')
print(x.json()) # We can get results in json format as well.

x = requests.get('https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png')
with open('google2.png', 'wb') as f:
    f.write(x.content)

