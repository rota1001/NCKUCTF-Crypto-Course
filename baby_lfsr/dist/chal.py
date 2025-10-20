from Crypto.Util.number import *
from secret import FLAG

def lfsr(mask):
    x = getRandomNBitInteger(512)
    while True:
        for _ in range(512):
            x = (x >> 1) | ((int(x & mask).bit_count() & 1) << 511)
        yield x


p = lfsr(bytes_to_long(FLAG))

k = [next(p) for i in range(2)]
print(k)
