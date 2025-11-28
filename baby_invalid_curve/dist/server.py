#!/usr/bin/python3
from Crypto.Util.number import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from secret import FLAG
import os

class Curve:
    def __init__(self, p, ab: tuple[int, int]):
        F = lambda x: x % p
        self.F = F
        self.p = p
        a, b = ab
        self.a = F(a)
        self.b = F(b)

    def on_curve(self, x, y, z):
        F = self.F
        if z == 0:
            return True  # point at infinity
        x, y = F(x), F(y)
        return F(y**2) == F(x**3 + self.a * x + self.b)

    def __repr__(self):
        return f"Curve(y^2 = x^3 + {self.a}*x + {self.b}) over {self.F}"


class Point:
    def __init__(self, x, y, curve: Curve, isInf=False):
        self.curve = curve
        F = curve.F
        self.p = curve.p

        if isInf:
            self.x = F(0)
            self.y = F(0)
            self.z = F(0)
        else:
            self.x = F(x)
            self.y = F(y)
            self.z = F(1)

    def is_infinity(self):
        return self.z == 0

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __neg__(self):
        if self.is_infinity():
            return self
        return Point(self.x, -self.y, self.curve)

    def __add__(self, Q):
        if not isinstance(Q, Point):
            raise TypeError("Can only add two Points")
        if self.curve != Q.curve:
            raise ValueError("Points are not on the same curve")

        if self.is_infinity():
            return Q
        if Q.is_infinity():
            return self

        x1, y1 = self.x, self.y
        x2, y2 = Q.x, Q.y
        F = self.curve.F
        p = self.curve.p

        if F(x1) == F(x2):
            if F(y1 + y2) == 0:
                return Point(0, 0, self.curve, isInf=True)
            else:
                # handle tangent (doubling)
                if F(y1) == 0:
                    return Point(0, 0, self.curve, isInf=True)
                a = self.curve.a
                lam = (3 * x1**2 + a) * pow(2 * y1, -1, p) % p
        else:
            lam = (y2 - y1) * pow(x2 - x1, -1, p) % p

        x3 = lam**2 - x1 - x2
        y3 = lam * (x1 - x3) - y1
        return Point(x3, y3, self.curve)

    def __repr__(self):
        if self.is_infinity():
            return "Point(infinity)"
        return f"Point({self.x}, {self.y})"

    def to_affine(self):
        if self.is_infinity():
            return None
        return (self.x, self.y)

    def __rmul__(self, k: int):
        k = int(k)
        if k < 0:
            return (-self).__rmul__(-k)

        result = Point(0, 0, self.curve, isInf=True)
        addend = self

        while k:
            if k & 1:
                result = result + addend
            addend = addend + addend
            k >>= 1

        return result
    def __lmul__(self, k: int):
        k = int(k)
        if k < 0:
            return (-self).__lmul__(-k)

        result = Point(0, 0, self.curve, isInf=True)
        addend = self

        while k:
            if k & 1:
                result = result + addend
            addend = addend + addend
            k >>= 1

        return result

def challenge():
    key = os.urandom(16)
    x = bytes_to_long(key)
    p = 72364592471999048991746278474134824829105489436651145838157001475268386866299
    a = 8604640036494654386860733898153642122179620931985649848848369802781091921371
    b = 56971794987620162734644006973338772666664821136381881122328067160515831408060
    G = (41812042345829448981995671495167223372573459468985716536568937365077238371758, 2499393139327142407391759590193587472717194978120088345893100098450726121503)
    E = Curve(p, (a, b))
    G = Point(G[0], G[1], E)
    y = x * G
    cipher = AES.new(key, AES.MODE_ECB)
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"p: {p}")
    print(f"G: {G}")
    print(f"y: {y}")
    print(f"cipher: {cipher.encrypt(pad(FLAG, 16)).hex()}")
    while True:
        p0 = int(input("x: "))
        p1 = int(input("y: "))
        P = Point(p0, p1, E)
        print(f"res: {x * P}")


if __name__ == "__main__":
    challenge()