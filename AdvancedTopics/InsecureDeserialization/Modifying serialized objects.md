[Insecure deserialization](../Insecure%20deserialization.md)

# Solution
Login via wiener:peter
Look in the cookie storage
Find session cookie
Decode from url, base64
change admin param, and encode back
```js
O:4:"User":2:{s:8:"username";s:6:"wiener";s:5:"admin";b:1;}
```

Delete carlos
