'''
GET / HTTP/2
Host: 0a6300f90489c72781907bc80060004e.web-security-academy.net
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://portswigger.net/
Connection: keep-alive
Cookie: session=RfneWdVA4m7NZEaqOjZ8bg7KMhE5gj1p
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: cross-site
'''

import requests
import bs4

DOMAIN = "0a6300f90489c72781907bc80060004e.web-security-academy.net"
url = f"https://{DOMAIN}/"

headers = {
    "Host": DOMAIN,
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
    "session": "RfneWdVA4m7NZEaqOjZ8bg7KMhE5gj1p"
}

def parse_posts_ids():
    response = requests.get(url, headers=headers, cookies=cookies)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    a_tags = soup.find_all('a', href=True)

    post_ids = []
    for a in a_tags:
        if a['href'].startswith('/post?postId='):
            if a['href'].split('=')[1] not in post_ids:
                post_ids.append(a['href'].split('=')[1])

    return post_ids

def parse_uuid_of_users_from_posts():
    uuids = []
    for post_id in parse_posts_ids():
        response = requests.get(f"{url}post?postId={post_id}", headers=headers, cookies=cookies)

        soup = bs4.BeautifulSoup(response.text, "html.parser")
        a_tags = soup.find_all('a', href=True)

        for a in a_tags:
            if a['href'].startswith('/blogs?userId='):
                if a['href'].split('=')[1] not in uuids:
                    uuids.append(a['href'].split('=')[1])

    print(uuids)
    return uuids



parse_uuid_of_users_from_posts()    
