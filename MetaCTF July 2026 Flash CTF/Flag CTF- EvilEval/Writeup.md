# Challenge Information
- Challenge Name: EvilEval
- Category: Other/Miscellaneous
- Difficulty: Medium
- Points: 200
- CTF: Flash CTF – July 2026

# Challenge Description
> EvilEval is billed as an escape-proof Python sandbox. Your tools are confiscated at the door, and nothing you type is meant to reach the world outside. It has held every visitor so far.

The challenge provides a Python-based sandbox where user input is evaluated using `eval()`.

The goal is to bypass the restrictions and make the expression return the correct value to retrieve the flag.

# Source Code Analysis
The important part of the code is:

```python
if check_number(inp) or check_black_list(inp) or check_rce(inp):
    log_message(client_socket, "Nope! This input is not allowed.")

elif eval(inp) != key:
    log_message(client_socket, "Incorrect!")

else:
    log_message(client_socket, FLAG)
```
The user input is directly passed into: 
```python
eval(inp)
```
This means we need to provide a Python expression whose output matches the secret key.

# Finding the Vulnerability

The server creates the key using:
```python
ct = time.ctime().encode()

key = int((b"flag" + ct).hex(), 16) % 255
```
The value depends only on the current system time.

The calculation is:
```
key = int(hex("flag" + current_time),16) % 255
```
Since the time value is predictable, we can reproduce the same key.

# Blacklist Protection

The server attempts to prevent attacks using:
```python
black_list = [
'+',
'-',
'*',
'/',
'%',
'import',
'os',
'sys',
'__',
'eval'
]
```
It also blocks numbers:
```python
def check_number(inp):
    for i in range(10):
        if str(i) in inp:
            return True
```
However, this protection is weak because it only checks for specific strings.

# Solution Approach
## 1. Calculate the expected key using the current time.

Example:
```python
import time

ct = time.ctime().encode()

key = int((b"flag" + ct).hex(),16) % 255

print(key)
```
## 2. Create a Python expression that evaluates to the same number while avoiding:
- digits
- blacklisted characters
- blocked keywords
## 3. Send the expression to the server.

If:
```python
eval(input) == key
```
the server returns the flag.

# Vulnerability

The main issue is:
```python
eval(user_input)
```
Using eval() on user-controlled input is dangerous because it allows arbitrary Python expression execution.
A blacklist cannot securely restrict Python code execution.

# Final Flag
```
MetaCTF{S4f3_3v4l_1s_4_Mu5t_1337}
```

# Lessons Learned
- Never use eval() with untrusted user input.
- Blacklist-based filtering is not a secure sandbox.
- Secrets should not depend on predictable values like timestamps.
- Proper sandboxing requires isolation instead of keyword filtering.
