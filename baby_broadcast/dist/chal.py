from Crypto.Util.number import *
from secret import FLAG

p1, q1 = getPrime(256), getPrime(256)
p2, q2 = getPrime(256), getPrime(256)
p3, q3 = getPrime(256), getPrime(256)

n1 = p1 * q1
n2 = p2 * q2
n3 = p3 * q3

e = 3

print(f"{n1 = }")
print(f"{n2 = }")
print(f"{n3 = }")
print(f"{e = }")

m = bytes_to_long(FLAG)
c1 = pow(m, e, n1)
c2 = pow(m, e, n2)
c3 = pow(m, e, n3)

print(f"{c1 = }")
print(f"{c2 = }")
print(f"{c3 = }")
