# Description

This lab is vulnerable to web cache poisoning. A victim user will view any comments that you post. To solve this lab, you need to poison the cache with a response that executes `alert(document.cookie)` in the visitor's browser. However, you also need to make sure that the response is served to the specific subset of users to which the intended victim belongs.

# Solution

```
HTTP/1.1 302 Found
Location: /post/comment/confirmation?postId=4
Vary: User-Agent
X-Frame-Options: SAMEORIGIN
Connection: close
Content-Length: 0
```

Vary header

## ParamMiner 

origin, x-host, x-host~%h:%s

## Analyze js

loadComments.js -> snippet
```js
commentBodyPElement.innerHTML = DOMPurify.sanitize(comment.body, {ALLOWED_TAGS: ['b', 'i', 'u', 'img', 'a'], ALLOWED_ATTR: ['src', 'href']});
```

as we can see, we can include tag `img` with attribute `src`

request
```
csrf=pffQiULRSMKqE0Aqq7kkxionac8EkI5R&postId=4&comment=<img%20src="/image/blog/posts/55.jpg"%20/>&name=hell&email=hell%40hello.com&website=
```

![](Attachments/Pasted%20image%2020240603214616.png)

![](Attachments/Pasted%20image%2020240603214622.png)

