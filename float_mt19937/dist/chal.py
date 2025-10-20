import random
from Crypto.Util.number import *
from secret import FLAG

k = [random.random() for i in range(700)]

print(k)

print(bytes_to_long(FLAG) ^ random.getrandbits(512))
