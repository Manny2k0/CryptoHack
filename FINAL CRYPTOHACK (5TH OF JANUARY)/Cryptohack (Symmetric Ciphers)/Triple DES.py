import requests
from Crypto.Util.Padding import unpad

def secure_flag(encryption_key):
    response = requests.get(f"http://aes.cryptohack.org/triple_des/encrypt_flag/{encryption_key.hex()}")
    return bytes.fromhex(response.json()['ciphertext'])

def secure_encrypt(encryption_key, plain_text):
    response = requests.get(f"http://aes.cryptohack.org/triple_des/encrypt/{encryption_key.hex()}/{plain_text.hex()}/")
    return bytes.fromhex(response.json()['ciphertext'])

# DES weak keys
des_key_one = b"\x01\x01\x01\x01\x01\x01\x01\x01"
des_key_two = b"\xfe\xfe\xfe\xfe\xfe\xfe\xfe\xfe"

# 3DES weak key = des_key_one||des_key_two
triple_des_key = des_key_one + des_key_two

secured_flag = secure_flag(triple_des_key)
decoded_flag = unpad(secure_encrypt(triple_des_key, secured_flag), 8)
print(decoded_flag.decode())