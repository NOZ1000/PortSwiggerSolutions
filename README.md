Port Swigger Labs Solutions only using `python` scripts.


# Authentification Labs
|Lab Name|Link|
|---|---|
|Broken brute-force protection, IP block|[click](ServerSide/Authentification/Broken%20brute-force%20protection%2C%20IP%20block/solve.py)|
|Username enumeration via account lock|[click](/ServerSide/Authentification/Username%20enumeration%20via%20account%20lock/solve.py)|
|Username enumeration via response timing|[click](/ServerSide/Authentification/Username%20enumeration%20via%20response%20timing/solve.py)|
|Username enumeration via subtly different responses|[click](/ServerSide/Authentification/Username%20enumeration%20via%20subtly%20different%20responses/solve.py)|
|Web shell content type restriction|[click](https://github.com/NOZ1000/PortSwiggerSolutions/blob/main/ServerSide/FileUpload/web_shell_content_type_rest/solve.py)|
|Broken brute-force protection, multiple credentials per request|[click](/ServerSide/Authentification/Broken%20brute-force%20protection,%20multiple%20credentials%20per%20request/solve.py)|
|Brute-forcing a stay-logged-in cookie|[click](/ServerSide/Authentification/Brute-forcing%20a%20stay-logged-in%20cookie/solve.py)|
|Password reset broken logic|[click](/ServerSide/Authentification/Password%20reset%20broken%20logic/solve.py)|
|Password reset poisoning via middleware|[click](/ServerSide/Authentification/Password%20reset%20poisoning%20via%20middleware/solve.py)|
|Offline password cracking|[click](/ServerSide/Authentification/Offline%20password%20cracking/solve.py)|
|Password brute-force via password change|[click](/ServerSide/Authentification/Password%20brute-force%20via%20password%20change/solve.py)|

# Path traversal
|Lab Name|Link|
|---|---|
|File path traversal, traversal sequences blocked with absolute path bypass|[click](/ServerSide/PathTraversal/File%20path%20traversal,%20traversal%20sequences%20blocked%20with%20absolute%20path%20bypass/solve.py)|
|File path traversal, traversal sequences stripped non-recursively|[click](/ServerSide/PathTraversal/File%20path%20traversal,%20traversal%20sequences%20stripped%20non-recursively/solve.py)|
|File path traversal, traversal sequences stripped with superfluous URL-decode|[click](/ServerSide/PathTraversal/File%20path%20traversal,%20traversal%20sequences%20stripped%20with%20superfluous%20URL-decode/solve.py)|
|File path traversal, validation of start of path|[click](/ServerSide/PathTraversal/File%20path%20traversal,%20validation%20of%20start%20of%20path/solve.py)|
|File path traversal, validation of file extension with null byte bypass|[click](/ServerSide/PathTraversal/File%20path%20traversal,%20validation%20of%20file%20extension%20with%20null%20byte%20bypass/solve.py)|

# OS command injection
|Lab Name|Link|
|---|---|
|OS command injection, simple case|[click](/ServerSide/OS%20command%20injection/OS%20command%20injection,%20simple%20case/solve.py)|
|Blind OS command injection with time delays|[click](/ServerSide/OS%20command%20injection/Blind%20OS%20command%20injection%20with%20time%20delays/solve.py)|
|Blind OS command injection with output redirection|[click](/ServerSide/OS%20command%20injection/Blind%20OS%20command%20injection%20with%20output%20redirection/solve.py)|

# Business logic vulnerabilities
|Lab Name|Link|
|---|---|
|Excessive trust in client-side controls|[click](/ServerSide/Business%20logic%20vulnerabilities/Excessive%20trust%20in%20client-side%20controls/solve.py)|
|High-level logic vulnerability|[click](/ServerSide/Business%20logic%20vulnerabilities/High-level%20logic%20vulnerability/solve.py)|
|Inconsistent security controls|[click](/ServerSide/Business%20logic%20vulnerabilities/Inconsistent%20security%20controls/solve.py)|
|Flawed enforcement of business rules|[click](/ServerSide/Business%20logic%20vulnerabilities/Flawed%20enforcement%20of%20business%20rules/solve.py)|
|Low-level logic flaw|[click](/ServerSide/Business%20logic%20vulnerabilities/Low-level%20logic%20flaw/solve.py)|
|Inconsistent handling of exceptional input|[click](/ServerSide/Business%20logic%20vulnerabilities/Inconsistent%20handling%20of%20exceptional%20input/solve.py)|
|Weak isolation on dual-use endpoint|[click](/ServerSide/Business%20logic%20vulnerabilities/Weak%20isolation%20on%20dual-use%20endpoint/solve.py)
|Insufficient workflow validation|[click](/ServerSide/Business%20logic%20vulnerabilities/Insufficient%20workflow%20validation/solve.md)|

# Access control
|Lab Name|Link|
|---|---|
|Method-based access control can be circumvented|[click](/ServerSide/AccessControl/Method-based%20access%20control%20can%20be%20circumvented/solve.py)|
|User ID controlled by request parameter, with unpredictable user IDs|[click](/ServerSide/AccessControl/User%20ID%20controlled%20by%20request%20parameter,%20with%20unpredictable%20user%20IDs%20/solve.py)|
|User ID controlled by request parameter with data leakage in redirect|[click](/ServerSide/AccessControl/User%20ID%20controlled%20by%20request%20parameter%20with%20data%20leakage%20in%20redirect/solve.py)|
|Multi-step process with no access control on one step|[click](/ServerSide/AccessControl/Multi-step%20process%20with%20no%20access%20control%20on%20one%20step/solve.py)|
|Referer-based access control|[click](/ServerSide/AccessControl/Referer-based%20access%20control/solve.py)|
|Web shell upload via race condition|[click](/ServerSide/FileUpload/Web%20shell%20upload%20via%20race%20condition/solve.py)|

# Race conditions
    Unfortunatly, my python exploit can successfully apply one coupon maximum 
    3 times, but to solve the lab, we need to apply it more than 20 times.
    So, I will solve it using Turbo Intruder using Single Packet Attack. 
    But i think that was nice try. In future i need to try use 
    this git repo https://github.com/nxenon/h2spacex?tab=readme-ov-file 
    to solve it using only python.
|Lab Name|Link|
|---|---|
|Limit overrun race conditions|[click](/ServerSide/Race%20conditions/Limit%20overrun%20race%20conditions/solve.py)|
|Bypassing rate limits via race conditions|[click](/ServerSide/Race%20conditions/Bypassing%20rate%20limits%20via%20race%20conditions/solve.md)|
|Multi-endpoint race conditions|[click](/ServerSide/Race%20conditions/Multi-endpoint%20race%20conditions/solve.md)|
|Single-endpoint race conditions|[click](/ServerSide/Race%20conditions/Single-endpoint%20race%20conditions/solve.md)|


# Server-side request forgery (SSRF)

|Lab Name|Link|
|---|---|
|Basic SSRF against another back-end system|[click](/ServerSide/SSRF/Basic%20SSRF%20against%20another%20back-end%20system/solve.py)|
|SSRF with blacklist-based input filter|[click](/ServerSide/SSRF/SSRF%20with%20blacklist-based%20input%20filter/solve.py)|

# XML external entity (XXE) injection

|Lab Name|Link|
|---|---|
|Exploiting XXE using external entities to retrieve files|[click](/ServerSide/XXE/Exploiting%20XXE%20using%20external%20entities%20to%20retrieve%20files/solve.py)|