from Crypto.Util.number import *
import random
from secret import FLAG

def genprimes():
    while True:
        p = 1
        while p.bit_length() < 256:
            p *= random.choice([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        p += 1
        if isPrime(p):
            break
    q = getPrime(256)
    return p, q

p, q = genprimes()
n = p * q
e = 0x10001

m = bytes_to_long(FLAG)

c = pow(m, e, n)

print(f"{e = }")
print(f"{n = }")
print(f"{c = }")
