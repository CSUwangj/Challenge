from Crypto.Util.number import *;
from pwn import xor

s = long_to_bytes(0x73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d)
for i in range(256):
    r = xor(s, i)
    if b'{' in r and b'}' in r:
        print(r)