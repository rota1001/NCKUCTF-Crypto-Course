from Crypto.Util.number import *
from secret import FLAG
p, q = getPrime(1024), getPrime(1024)

m = bytes_to_long(FLAG)
p0 = p >> 128

n = p * q
e = 0x10001

c = pow(m, e, n)

print(f"{e = }")
print(f"{n = }")
print(f"{c = }")
print(f"{p0 = }")
