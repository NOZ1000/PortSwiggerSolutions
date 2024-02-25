from hyper import HTTPConnection

# Connect to the server using HTTP/2
conn1 = HTTPConnection('127.0.0.1:8000')
conn2 = HTTPConnection('127.0.0.1:8000')

# Send HTTP requests
conn1.request('GET', '/hello.txt')
conn2.request('GET', '/hello2.txt')

# Get responses
response1 = conn1.get_response()
response2 = conn2.get_response()

# Print responses
print("Response from /hello.txt:", response1.read().decode())
print("Response from /hello2.txt:", response2.read().decode())
