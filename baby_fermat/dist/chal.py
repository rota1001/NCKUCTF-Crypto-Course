from Crypto.Util.number import *
from secret import FLAG

def genprimes():
    p = getPrime(256)
    q = p + 1
    while not isPrime(q):
        q += 1
    return p, q

p, q = genprimes()
n = p * q
e = 0x10001

m = bytes_to_long(FLAG)

c = pow(m, e, n)

print(f"{e = }")
print(f"{n = }")
print(f"{c = }")
