#!/usr/bin/python3
from secret import FLAG
import random
from Crypto.Cipher import AES
import os

def encrypt(key: bytes):
    x = input("message: ").strip().encode()
    if len(x) % 16 != 0:
        print("Not aligned")
        exit(1)
    if b"give me the flag" in x:
        print("Bad Hacker")
        exit(1)
    cipher = AES.new(key, AES.MODE_ECB)
    print(cipher.encrypt(x).hex())

def get_flag(key: bytes):
    x = bytes.fromhex(input("cipher: ").strip())
    if len(x) % 16 != 0:
        print("Not aligned")
        exit(1)
    cipher = AES.new(key, AES.MODE_ECB)
    if b"give me the flag" not in cipher.decrypt(x):
        print("Something Wrong")
        exit(1)
    print(FLAG)

def challenge():
    key = os.urandom(16)
    for _ in range(2):
        print("Please input your choice:")
        print("[1] Encrypt")
        print("[2] Get Flag")
        mode = input("> ")
        if "1" in mode:
            encrypt(key)
        else:
            get_flag(key)

    

if __name__ == "__main__":
    challenge()
