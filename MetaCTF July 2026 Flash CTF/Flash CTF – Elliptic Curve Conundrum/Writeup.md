# Challenge Information
- Challenge Name: Elliptic Curve Conundrum
- Category: Cryptography
- Difficulty: Easy
- Points: 150
- CTF: Flash CTF – July 2026

# Challenge Description
```
Every message that leaves the courier's office carries his personal seal, a mark he swears is impossible to forge.
He's confident nobody could ever imitate his hand, but is he right?
```
The server provides an ECDSA signing service. It allows:
- Viewing the public key.
- Getting a message signed.

The goal is to recover the private key, which is also the flag.

# Source Code Analysis
The server generates an ECDSA private key:
```python
d = bytes_to_long(flag)

pub_key = ecdsa.ecdsa.Public_key(gen, gen * d)
priv_key = ecdsa.ecdsa.Private_key(pub_key, d)
```
The private key is directly derived from the flag.

So recovering d gives us: Flag

# Understanding ECDSA

ECDSA signing uses:

- d → Private key
- m → Message
- k → Random nonce
- (r,s) → Signature

The signature is generated as:
```
r=(kG)x modn
s=k^(−1)(m+dr)modn
```
where:

G is the generator point.
n is the curve order.

# Solution
```python
#!/usr/bin/env python3
import random
import time
import ecdsa
from pwn import *  # pip install pwntools

try:
    from Crypto.Util.number import long_to_bytes  # type: ignore[import-not-found]
except ImportError:
    def long_to_bytes(value: int) -> bytes:
        return value.to_bytes((value.bit_length() + 7) // 8 or 1, "big")

# Initialize secp256k1 curve parameters
gen = ecdsa.SECP256k1.generator
order = gen.order()

# Target server details (Replace with your actual CTF host)
HOST = 'Hostname or IP Address'  # e.g., 'example.com'
PORT = 1337

print(f"[*] Establishing TLS connection to {HOST}:{PORT}...")

# 1. Establish the TLS connection using your snippet
# ssl=True triggers the TLS handshake required for SNI routing endpoints
io = remote(HOST, PORT, ssl=True)

# Record local time immediately upon a successful handshake
# This serves as our anchor point for brute-forcing the server's time seed
approx_server_time = int(time.time())

# Read the greeting banner up to the first input prompt
io.recvuntil(b'option > ')

# 2. Interact with the menu: Select Option 2 to request a signature
io.sendline(b'2')
io.sendlineafter(b'msg > ', b'A')  # Provide a dummy string to sign

# 3. Parse and extract the mathematical elements from the TLS stream
io.recvuntil(b'msg = ')
msg_val = int(io.readline().strip())

io.recvuntil(b'r,s = (')
sig_data = io.readline().decode().strip().rstrip(')').split(',')
r_val = int(sig_data[0])
s_val = int(sig_data[1])

io.close()

print(f"\n[+] Extracted TLS Data Elements:")
print(f"    Padded Msg Int: {msg_val}")
print(f"    Signature r:    {r_val}")
print(f"    Signature s:    {s_val}\n")
print("[*] Launching PRNG Time-Seed Sync...")

# 4. Search a +/- 30 second window to account for network latency and clock drift
found_flag = False
for potential_seed in range(approx_server_time - 30, approx_server_time + 30):
    random.seed(potential_seed)
    guessed_k = random.getrandbits(255)
    
    # Mathematical validation check: Validate if guessed_k * G yields X-coordinate 'r'
    guessed_R_point = guessed_k * gen
    if int(guessed_R_point.x()) == r_val:
        print(f"[+] Cryptographic Match Found!")
        print(f"    Verified Server Time Seed: {potential_seed}")
        print(f"    Reconstructed Secret Nonce (k): {guessed_k}")
        
        # 5. Extract private key d using the modular relationship:
        # d = ((s * k) - msg) * r^-1 mod order
        r_inv = pow(r_val, -1, order)
        d_val = ((s_val * guessed_k - msg_val) * r_inv) % order
        
        # Convert the private key integer back to text bytes
        flag_bytes = long_to_bytes(d_val)
        print(f"\n[SUCCESS] Decrypted Private Key Flag:")
        print(f"MetaCTF{{{flag_bytes.decode(errors='ignore')}}}")
        found_flag = True
        break

if not found_flag:
    print("[-] Exploit failed. The server's clock may be outside the current time window.")

```
## Exploit Code Explanation

The exploit script takes advantage of the predictable ECDSA nonce generation vulnerability.

The server generates the ECDSA nonce using Python's `random` module, which is seeded with the current timestamp:

```python
random.seed(int(time.time()))
```

# Flag Recovered
```
MetaCTF{R3u51ng_n0nc3_4nd_c0nn3ct1on?!?!}
```

# Tools Used
1. Python
2. Pwntools
3. ECDSA mathematics
4. Modular arithmetic

# Key Takeaways
- ECDSA security depends on secure nonce generation.
- Never use predictable PRNGs for cryptographic operations.
- A leaked nonce can reveal the private key.
- Time-based randomness is not suitable for cryptographic purposes.
- Always use secure randomness sources such as os.urandom() or RFC6979 deterministic signing.
