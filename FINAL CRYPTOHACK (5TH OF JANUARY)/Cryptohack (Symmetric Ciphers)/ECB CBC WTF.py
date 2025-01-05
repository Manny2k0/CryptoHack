import json
import requests

ENCRYPTION_ENDPOINT = "http://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/"
DECRYPTION_ENDPOINT = "http://aes.cryptohack.org/ecbcbcwtf/decrypt/{cipher}/"

def fetch_ciphertext(message):
    response = requests.get(ENCRYPTION_ENDPOINT)
    data = json.loads(response.text)
    return data['ciphertext']

def fetch_plaintext(cipher_text):
    response = requests.get(DECRYPTION_ENDPOINT.format(cipher=cipher_text))
    data = json.loads(response.text)
    return data['plaintext']

def xor_bytes(byte_seq1, byte_seq2):
    return [b1 ^ b2 for b1, b2 in zip(byte_seq1, byte_seq2)]

cipher_text = fetch_ciphertext('Dont care')
cipher_segments = [cipher_text[i:i+32] for i in range(0, len(cipher_text), 32)]  # [0] is the IV, [1] and subsequent are the encryptions of the plaintext blocks.

plain_text_blocks = [0]*(len(cipher_segments) - 1)
for idx in range(len(plain_text_blocks)):
    decrypted_bytes = bytes.fromhex(fetch_plaintext(cipher_segments[idx+1]))
    iv_bytes = bytes.fromhex(cipher_segments[idx])
    plain_text_blocks[idx] = ''.join(map(chr, xor_bytes(decrypted_bytes, iv_bytes)))

print(f"Flag: {''.join(plain_text_blocks)}")