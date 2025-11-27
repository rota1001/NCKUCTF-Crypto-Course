from Crypto.Util.number import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from sage.all import *
import os
from secret import FLAG

def max_fact(n: int):
    return max(p for p, e in factor(n))

def gen_curve():
    p = random_prime(2**150 - 1)
    F = GF(p)
    while True:
        a = F(randint(1, p - 1))
        b = F(randint(1, p - 1))
        if (4 * a**3 + 27 * b**2) == 0:
            continue
        E = EllipticCurve(F, [a, b])
        ord = E.order()
        if max_fact(ord) > 10**10:
            continue
        return a, b, p

key = os.urandom(16)

a, b, p = gen_curve()
E = EllipticCurve(GF(p), [a, b])
G = E.gens()[0]
x = bytes_to_long(key)
y = x * G

cipher = AES.new(key, AES.MODE_ECB)

print(f"G = {G.xy()}")
print(f"{a = }")
print(f"{b = }")
print(f"{p = }")
print(f"y = {y.xy()}")
print(f"c = {cipher.encrypt(pad(FLAG, 16)).hex()}")
