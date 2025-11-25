from sage.all import *
from Crypto.Util.number import *
from secret import FLAG

class SingularCurve:
    def __init__(self, F, ab: tuple[int, int]):
        self.F = F
        a, b = ab
        self.a = F(a)
        self.b = F(b)

    def on_curve(self, x, y, z):
        F = self.F
        if z == 0:
            return True  # point at infinity
        x, y = F(x), F(y)
        return y**2 == x**3 + self.a * x + self.b

    def __repr__(self):
        return f"SingularCurve(y^2 = x^3 + {self.a}*x + {self.b}) over {self.F}"


class SingularPoint:
    def __init__(self, x, y, curve: SingularCurve, isInf=False):
        self.curve = curve
        F = curve.F

        if isInf:
            self.x = F(0)
            self.y = F(0)
            self.z = F(0)
        else:
            self.x = F(x)
            self.y = F(y)
            self.z = F(1)
            if not curve.on_curve(self.x, self.y, self.z):
                print(f"[!] WARNING: ({x}, {y}) is not on the curve")

    def is_infinity(self):
        return self.z == 0

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __neg__(self):
        if self.is_infinity():
            return self
        return SingularPoint(self.x, -self.y, self.curve)

    def __add__(self, Q):
        if not isinstance(Q, SingularPoint):
            raise TypeError("Can only add two SingularPoints")
        if self.curve != Q.curve:
            raise ValueError("Points are not on the same curve")

        if self.is_infinity():
            return Q
        if Q.is_infinity():
            return self

        x1, y1 = self.x, self.y
        x2, y2 = Q.x, Q.y
        F = self.curve.F

        if x1 == x2:
            if y1 + y2 == 0:
                return SingularPoint(0, 0, self.curve, isInf=True)
            else:
                # handle tangent (doubling)
                if y1 == 0:
                    return SingularPoint(0, 0, self.curve, isInf=True)
                a = self.curve.a
                lam = (3 * x1**2 + a) / (2 * y1)
        else:
            lam = (y2 - y1) / (x2 - x1)

        x3 = lam**2 - x1 - x2
        y3 = lam * (x1 - x3) - y1
        return SingularPoint(x3, y3, self.curve)

    def __repr__(self):
        if self.is_infinity():
            return "SingularPoint(infinity)"
        return f"SingularPoint({self.x}, {self.y})"

    def to_affine(self):
        if self.is_infinity():
            return None
        return (self.x, self.y)

    def __rmul__(self, k: int):
        k = int(k)
        if k < 0:
            return (-self).__rmul__(-k)

        result = SingularPoint(0, 0, self.curve, isInf=True)
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

        result = SingularPoint(0, 0, self.curve, isInf=True)
        addend = self

        while k:
            if k & 1:
                result = result + addend
            addend = addend + addend
            k >>= 1

        return result

p = 9050530688715247120969729628492380160042134997240313989906806042561926071086167885723573703694486269088911077994875609728623164679961224421421355584310447
a = 0
b = 0
E = SingularCurve(GF(p), (a, b))
print("Notice that this curve equals to y^2 = x^3")
x = bytes_to_long(FLAG)
G = SingularPoint(4, 8, E)

y = x * G
print(f"{a = }")
print(f"{b = }")
print(f"{p = }")
print(f"{G = }")
print(f"{y = }")
