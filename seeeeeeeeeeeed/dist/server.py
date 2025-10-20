#!/usr/bin/python3
from secret import FLAG
import random
import os

def challenge():
    seed = 0
    while True:
        print("Please input your choice:")
        print("[1] modify seed")
        print("[2] check")
        mode = input("> ")
        if "1" in mode:
            x = int(input("Input x: "))
            seed <<= 32
            seed += x
        elif "2" in mode:
            break
        else:
            print("Unknown Command")
    
    random.seed(seed)
    rands = [random.getrandbits(32) for i in range(623)]
    for i, j in zip(rands, rands[1:]):
        if i != j:
            print("Fail")
            exit(1)
    print("Success!!")
    print(f"The flag is: {FLAG.decode()}")

    

if __name__ == "__main__":
    challenge()
