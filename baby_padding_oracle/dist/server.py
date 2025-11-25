#!/usr/bin/python3
from secret import FLAG
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def challenge():
    key = os.urandom(16)
    iv = os.urandom(16)
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    print(f"ciphertext: {cipher.encrypt(pad(FLAG, 16)).hex()}")
    print(f"iv: {iv.hex()}")
    while True:
        x = bytes.fromhex(input("Give me the ciphertext: ").strip())
        cipher = AES.new(key, AES.MODE_CBC, iv)
        try:
            unpad(cipher.decrypt(x), 16)
            print("Success")
        except:
            print("Fail")



if __name__ == "__main__":
    challenge()
