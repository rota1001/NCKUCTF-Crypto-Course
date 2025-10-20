from sage.all import *
from Crypto.Util.number import *
from pwn import *

from sage.matrix.matrix2 import Matrix
def resultant(f1, f2, var):
    # Copied from https://jsur.in/posts/2021-07-19-google-ctf-2021-crypto-writeups#h1
    return Matrix.determinant(f1.sylvester_matrix(f2, var))

def func1(x, y, z):
    return x * y**4 + y**2 + x * z

def func2(x, y, z):
    return x * y * z ** 3 + y * z + x

def func3(x, y, z):
    return x + y + x * z

r = remote("127.0.0.1", 10005)

r.recvuntil(b" = ")
p = int(r.recvline().strip().decode())
r.recvuntil(b" = ")
a = int(r.recvline().strip().decode())
r.recvuntil(b" = ")
b = int(r.recvline().strip().decode())
r.recvuntil(b" = ")
c = int(r.recvline().strip().decode())


P = PolynomialRing(GF(p), "x,y,z")
x, y, z = P.gens()

f = func1(x, y, z) - a
g = func2(x, y, z) - b
h = func3(x, y, z) - c


fx = P.remove_var(y, z)(resultant(resultant(f, g, z), resultant(f, h, z), y))

x_sol = int(fx.roots()[0][0])

fx = x - x_sol

fy = P.remove_var(x, z)(resultant(resultant(f, g, z), fx, x))
y_sol = int(fy.roots()[0][0])

fy = y - y_sol

fz = P.remove_var(x, y)(resultant(resultant(f, fx, x), fy, y))
z_sol = int(fz.roots()[0][0])


print(f(x_sol, y_sol, z_sol))
print(g(x_sol, y_sol, z_sol))
print(h(x_sol, y_sol, z_sol))
payload = f"{x_sol}, {y_sol}, {z_sol}".encode()

r.sendlineafter(b": ", payload)
r.interactive()
# print(fx.roots())
