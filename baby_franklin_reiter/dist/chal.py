from Crypto.Util.number import *
from secret import FLAG

p, q = getPrime(256), getPrime(256)

n = p * q
e = 37
m = bytes_to_long(FLAG)
c1 = pow(m, e, n)
c2 = pow(12345 * m + 54321, e, n)

print(f"{e = }")
print(f"{n = }")
print(f"{c1 = }")
print(f"{c2 = }")
