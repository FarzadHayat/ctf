#!/usr/bin/env python

from pwn import *

flag_enc = bytes.fromhex(
    "551257106e1a52095f654f510a6b4954026c1e0304394100043a1c5654505b6b"
)
text_enc = bytes.fromhex(
    "236625611d392070281d3971731d3922251d3923201d3922751d392423702f1d"
)
text_dec = "A" * 32

key = xor(text_enc, text_dec)  # XOR is transitive

flag_dec = xor(key, flag_enc).decode()

flag = "picoCTF{" + flag_dec + "}"
print(flag)
