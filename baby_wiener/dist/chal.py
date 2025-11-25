from Crypto.Util.number import *
from secret import FLAG

p, q = getPrime(256), getPrime(256)

n = p * q
d = getPrime(30)
e = pow(d, -1, (p - 1) * (q - 1))
m = bytes_to_long(FLAG)
c = pow(m, e, n)

print(f"{e = }")
print(f"{n = }")
print(f"{c = }")
