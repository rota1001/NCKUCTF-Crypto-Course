#!/usr/bin/python3
from secret import FLAG
import random
from Crypto.Util.number import *

def challenge():
    for i in range(10):
        a = random.randint(1, 100000000000000000000000000000)
        b = random.randint(1, 1000000000000000000000000000000)
        print(f"a = {bytes_to_long(str(a).encode())}")
        print(f"b = {str(b).encode().hex()}")
        c = int(input("give me c: "))
        if a + b != c:
            print("fail")
            exit(1)
    print(FLAG)

if __name__ == '__main__':
    challenge()