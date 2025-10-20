import random
from Crypto.Util.number import *
from secret import FLAG

k = [random.getrandbits(32) for i in range(624)]

print(k)

print(bytes_to_long(FLAG) ^ random.getrandbits(512))
