#!/usr/bin/python3
FLAG = b"NCKUCTF{LEAKFLKJDSKDJFSLKDFLDKKDSJFKDS}"

from hashlib import *
import os

def hash1(x: bytes):
    return md5(x).digest()

def hash2(x: bytes):
    return sha1(x).digest()

def hash3(x: bytes):
    return sha256(x).digest()

def hash4(x: bytes):
    return sha512(x).digest()

def challenge(hash):
    m = os.urandom(16)
    print(f"hash: {hash(m).hex()}")
    evil_text = bytes.fromhex(input())
    evil_hash = bytes.fromhex(input())
    if hash(m + evil_text) != evil_hash:
        print("HASH ERROR!!")
        return False
    if b"give me the flag" not in evil_text:
        print("SOMETHING WRONG?")
        return False
    return True
def challenges():
    for hash in [hash1, hash2, hash3, hash4]:
        if not challenge(hash):
            print("Bad hacker")
            return
    print(f"The flag is: {FLAG.decode()}")
    


if __name__ == "__main__":
    challenges()
