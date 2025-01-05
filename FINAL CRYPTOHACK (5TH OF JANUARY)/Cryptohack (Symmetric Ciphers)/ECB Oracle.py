import requests
from Crypto.Util.Padding import pad

encryption_endpoint = 'https://aes.cryptohack.org/ecb_oracle/encrypt/'

def encrypt_data(data_input):
    if isinstance(data_input, str):
        data_input = data_input.encode()

    return requests.get(encryption_endpoint + data_input.hex() + '/').json()['ciphertext']

initial_cipher_text = '\x00' * 16

original_length = len(encrypt_data(initial_cipher_text)) // 2

while True:
    initial_cipher_text += '\x00'
    current_length = len(encrypt_data(initial_cipher_text)) // 2

    if current_length != original_length:
        flag_length = current_length - 16 - len(initial_cipher_text)  # Padding and prefix length
        break

print('Flag length is', flag_length)

recovered_flag = bytes()

for position in range(flag_length):
    for ascii_val in range(32, 127):
        plaintext_block = pad(bytes([ascii_val]) + recovered_flag, 16)
        plaintext_block += b'A' * ((position + 1 - flag_length) % 16)

        response_data = encrypt_data(plaintext_block)

        negative_index = -((position + 1) // 16 + 1)

        if negative_index == -1:
            oracle_segment = response_data[-32:]
        else:
            oracle_segment = response_data[32*negative_index:32*(negative_index+1)]

        if response_data[:32] == oracle_segment:
            recovered_flag = bytes([ascii_val]) + recovered_flag
            print(recovered_flag.decode())
            break