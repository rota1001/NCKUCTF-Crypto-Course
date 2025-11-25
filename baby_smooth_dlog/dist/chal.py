from Crypto.Util.number import *
from secret import FLAG
def genPrime():
    while True:
        p = 2
        factors = []
        while p.bit_length() < 512:
            pi = getPrime(16)
            p *= pi
            factors.append(pi)
        p += 1
        success = True
        for i in factors:
            if pow(2, (p - 1) // i, p) == 1:
                success = False
        
        if isPrime(p) and success:
            break
    return p


p = genPrime()
g = 2
x = bytes_to_long(FLAG)
y = pow(g, x, p)
print(f"{p = }")
print(f"{y = }")