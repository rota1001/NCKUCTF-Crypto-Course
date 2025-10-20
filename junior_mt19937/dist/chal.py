import random
from Crypto.Util.number import *
from secret import FLAG

k = [random.getrandbits(31) for i in range(1500)]

print(k)

x = random.getrandbits(512)
print(bytes_to_long(FLAG) ^ x)