from Crypto.Util.number import *
from pwn import *


r = remote("127.0.0.1", 10005)
for i in range(10):
    r.recvuntil(b"= ")
    a = int(long_to_bytes(int(r.recvline().strip().decode())).decode())
    r.recvuntil(b"= ")
    b = int(bytes.fromhex(r.recvline().strip().decode()))
    c = a + b
    r.sendlineafter(b": ", str(c).encode())

r.interactive()