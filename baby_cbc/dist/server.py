#!/usr/bin/python3
from secret import FLAG
import random
from Crypto.Cipher import AES
import os

def encrypt(key: bytes, iv: bytes):
    x = bytes.fromhex(input("message: ").strip())
    if len(x) % 16 != 0:
        print("Not aligned")
        exit(1)
    if b"give me the flag" in x:
        print("Bad Hacker")
        exit(1)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    print(cipher.encrypt(x).hex())

def get_flag(key: bytes, iv: bytes):
    x = bytes.fromhex(input("cipher: ").strip())
    if len(x) % 16 != 0:
        print("Not aligned")
        exit(1)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    if b"give me the flag" not in cipher.decrypt(x):
        print("Something Wrong")
        exit(1)
    print(FLAG)
    exit(0)

def challenge():
    key = os.urandom(16)
    iv = os.urandom(16)
    for _ in range(3):
        print("Please input your choice:")
        print("[1] Encrypt")
        print("[2] Get Flag")
        mode = input("> ")
        if "1" in mode:
            encrypt(key, iv)
        else:
            get_flag(key, iv)

    

if __name__ == "__main__":
    challenge()
