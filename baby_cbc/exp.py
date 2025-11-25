from pwn import *

r = remote("localhost", 10005)

def xor(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))

# First: m = (nonce1 || m1)
# E(nonce1 ^ iv) = c1
# E(m1 ^ c1) = c2

# Second: m = (nonce1 || (c1 ^ c2 ^ m2))
# E(nonce1 ^ iv) = c1
# E((c1 ^ c2 ^ m2) ^ c1) = E(c2 ^ m2) = c3

target = b"ggive me the fla" + b"g" * 16

r.sendlineafter(b"> ", b"1")

nonce1 = b"a" * 16
m1 = target[:16]
m2 = target[16:]
r.sendlineafter(b":", (nonce1 + target[:16]).hex().encode())

rec = bytes.fromhex(r.recvline().strip().decode())
c1, c2 = rec[:16], rec[16:]

r.sendlineafter(b"> ", b"1")
r.sendlineafter(b":", (nonce1 + xor(xor(c1, c2), m2)).hex().encode())

rec = bytes.fromhex(r.recvline().strip().decode())
c3 = rec[16:]
r.sendlineafter(b"> ", b"2")
r.sendlineafter(b":", (c1 + c2 + c3).hex().encode())
r.interactive()
