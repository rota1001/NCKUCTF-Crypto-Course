import random

random.seed(0xdeadbeef)
a = [random.getrandbits(32) for _ in range(2)]
print(hex(a[1]), hex(a[0]))

random.seed(0xdeadbeef)
print(hex(random.getrandbits(64)))