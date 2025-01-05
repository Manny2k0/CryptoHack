from pwn import xor as bitwise_xor

cipher_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
cipher_bytes = bytes.fromhex(cipher_hex)

for key in range(256):
    decrypted_message = bitwise_xor(cipher_bytes, key)
    if decrypted_message[0:6] == b'crypto':
        print(key, decrypted_message)
        break