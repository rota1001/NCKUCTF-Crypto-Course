from Crypto.Util.number import *
from Crypto.Cipher import AES
from sage.all import *

G = (365776041158099525175541442273253364054421475, 481802054135332110916837074401691119736746084)
a = 279807575460102080696275727462812992458658885
b = 516607082167677821972035838069292942208896690
p = 535992773952533434651575401339912903558938417
y = (227995101454757710608005052752660327683160508, 375114850776676006811305947733474563794393761)
c = "27459f690dd919cc874eb12118b7757fd0d23ea244390d54c1d523035fdffd1be5fa0bebdb5c06dd60cd2c7e028b186c"
c = bytes.fromhex(c)

E = EllipticCurve(GF(p), [a, b])
G = E(G)
y = E(y)

primes = []
for i, j in factor(G.order()):
    primes.append(i ** j)

sol = []
for prime in primes:
    t = int(G.order() / prime)
    sol.append(discrete_log(t * y, t * G, operation="+"))

key = long_to_bytes(crt(sol, primes))
cipher = AES.new(key, AES.MODE_ECB)
flag = cipher.decrypt(c)
print(flag)
