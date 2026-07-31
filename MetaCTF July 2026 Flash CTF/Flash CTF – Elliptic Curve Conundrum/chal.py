#!/usr/bin/env python

import os
import random
import time

import ecdsa
from Crypto.Util.number import bytes_to_long
from os import urandom

# The flag itself is the ECDSA private key — recover it via nonce reuse.
FLAG = os.environ.get('FLAG', 'MetaCTF{Fake_Flag_For_Testing}')
flag = FLAG.split('{', 1)[1].rstrip('}').encode()

gen = ecdsa.SECP256k1.generator
order = gen.order()
d = bytes_to_long(flag)

pub_key = ecdsa.ecdsa.Public_key(gen, gen * d)
priv_key = ecdsa.ecdsa.Private_key(pub_key, d)

random.seed(int(time.time()))

print('Welcome to our ECDSA server!')
print('You have 2 options for your queries — make them count:')
print('\t1) View your public key.')
print('\t2) Retrieve a message.')
print()

for i in range(3):
    try:
        option = int(input('option > '))

        if option == 1:
            x = pub_key.point.x()
            y = pub_key.point.y()
            print(f'dG = ({x},{y})')

        elif option == 2: 
            nonce = random.getrandbits(255)
            msg   = input('msg > ').encode()
            padding = urandom(32 - len(msg))
            msg = bytes_to_long(msg + padding)
            sig = priv_key.sign(msg, nonce)
            print(f'{msg = }')
            print(f'r,s = ({sig.r},{sig.s})')

    except:
        print('Error :(')
