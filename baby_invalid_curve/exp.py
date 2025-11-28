from pwn import *
from sage.all import *
from Crypto.Util.number import *
from Crypto.Cipher import AES
r = remote("localhost", 10005)
# r = process(["python", "dist/server.py"])


r.recvuntil(b": ")
a = int(r.recvline().strip())
r.recvuntil(b": ")
b = int(r.recvline().strip())
r.recvuntil(b": ")
p = int(r.recvline().strip())
r.recvuntil(b": ")
r.recvuntil(b"t(")
G = tuple(map(int, r.recvline().strip(b")\n").decode().split(", ")))
r.recvuntil(b": ")
r.recvuntil(b"t(")
y = tuple(map(int, r.recvline().strip(b")\n").decode().split(", ")))

r.recvuntil(b": ")
ciphertext = bytes.fromhex(r.recvline().strip().decode())

proof.arithmetic(False)
yees = []
prods = 1
done = False
for b in range(1, 100):
    if done:
        break
    try:
        if (4 * a**3 + 27 * b**2) % p == 0:
            continue
        E = EllipticCurve(GF(p), [a, b])
        G = E.gens()[0]
        ord = E.order()
        for pp, e in factor(ord):
            if pp**e < 2**40:
                if gcd(prods, pp) != 1:
                    continue
                prods *= pp**e
                if prods > 2**257:
                    done = True
                print(pp**e)
                yees.append((G.xy(), b, pp**e, ord))
    except:
        pass
with open("tmp.txt", "w") as f:
    f.write(str(yees))

sols = []
primes = []

for G, b, pp, ord in yees:
    r.sendlineafter(b": ", str(G[0]).encode())
    r.sendlineafter(b": ", str(G[1]).encode())
    r.recvuntil(b"(")
    P = tuple(map(int, r.recvline().strip(b")\n").decode().split(", ")))
    print(a, b)
    try:
        E = EllipticCurve(GF(p), [a, b])
        G = E(G)
        P = E(P)
        sol = discrete_log((ord // pp) * P, (ord // pp) * G, ord=pp, operation="+")
        sols.append(sol)
        primes.append(pp)
    except:
        pass
sol = crt(sols, primes)
key = long_to_bytes(sol)
assert(len(key) == 16)


cipher = AES.new(key, AES.MODE_ECB)
flag = cipher.decrypt(ciphertext)
print(flag)

r.interactive()
