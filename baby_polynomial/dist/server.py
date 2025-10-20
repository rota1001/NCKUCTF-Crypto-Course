#!/usr/bin/python3
from Crypto.Util.number import *
from secret import FLAG
import random
import os

def func1(x, y, z, p):
    return (x * y**4 + y**2 + x * z) % p

def func2(x, y, z, p):
    return (x * y * z ** 3 + y * z + x) % p

def func3(x, y, z, p):
    return (x + y + x * z) % p

def challenge():
    p = getPrime(128)
    x, y, z = getRandomRange(1, p), getRandomRange(1, p), getRandomRange(1, p)
    a = func1(x, y, z, p)
    b = func2(x, y, z, p)
    c = func3(x, y, z, p)

    print(f"{p = }")
    print(f"{a = }")
    print(f"{b = }")
    print(f"{c = }")

    x, y, z = list(map(int, input("input x, y, z: ").strip().split(", ")))
    if a == func1(x, y, z, p) and b == func2(x, y, z, p) and c == func3(x, y, z, p):
        print("Success!!!")
        print(f"The flag is {FLAG.decode()}")
    else:
        print("Something Wrong")
    

if __name__ == "__main__":
    challenge()
