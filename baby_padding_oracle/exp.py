from pwn import *

r = remote("localhost", 10005)

def xor(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))

def check(iv: bytes, c: bytes):
    r.sendlineafter(": ", (iv + c).hex().encode())
    return b"Success" in r.recvline()

def decrypt_block(last_block: bytes, now: bytes) -> bytes:
    iv = [0 for i in range(16)]
    for i in range(1, 0x11):
        for j in range(0x100):
            iv[16 - i] = j
            if check(bytes(iv), now):
                break
        if i != 0x10:
            iv = list(xor(xor(bytes(iv), bytes([i for _ in range(16)])), bytes([i + 1 for _ in range(16)])))
    return xor(xor(last_block, iv), b"\x10" * 16)

def decrypt(ciphertext: bytes) -> bytes:
    plaintext = b""
    for i in range(0, len(ciphertext) - 16, 16):
        plaintext += decrypt_block(ciphertext[i: i + 16], ciphertext[i + 16: i + 32])
    return plaintext

r.recvuntil(b": ")
ciphertext = bytes.fromhex(r.recvline().strip().decode())
r.recvuntil(b": ")
iv = bytes.fromhex(r.recvline().strip().decode())

print(decrypt(iv + ciphertext))

r.interactive()
