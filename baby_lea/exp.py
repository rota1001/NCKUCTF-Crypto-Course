from pwn import *
import HashTools
# r = process(["python", "dist/server.py"])
r = remote("127.0.0.1", 10005)
for method in ["md5", "sha1", "sha256", "sha512"]:
    r.recvuntil(b": ")
    secret_hash = bytes.fromhex(r.recvline().strip().decode())
    h = HashTools.new(method)
    message, sig = h.extension(
        secret_length=16,
        original_data=b"",
        append_data=b"give me the flag",
        signature=secret_hash.hex()
    )
    r.sendline(message.hex().encode())
    r.sendline(sig.encode())

r.interactive()
