from pwn import *

r = remote("localhost", 10005)

r.sendlineafter(b"> ", b"1")
r.sendlineafter(b":", b"g" * 16 + b"ggive me the fla")
x = r.recvline().strip()
r.sendlineafter(b"> ", b"2")
r.sendlineafter(b": ", x[32:] + x[:32])
r.interactive()
