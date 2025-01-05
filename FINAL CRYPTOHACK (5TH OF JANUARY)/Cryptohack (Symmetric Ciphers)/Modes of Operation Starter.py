import requests

# Send GET request to retrieve encrypted flag
url_encrypt = "http://aes.cryptohack.org/block_cipher_starter/encrypt_flag/"
encryption_response = requests.get(url_encrypt)

# Extract the encrypted ciphertext from the response
cipher_data = encryption_response.json()
ciphertext = cipher_data['ciphertext']

# Display the received encrypted data
print("Encrypted ciphertext:", ciphertext)

# Send GET request to decrypt the ciphertext
url_decrypt = f"http://aes.cryptohack.org/block_cipher_starter/decrypt/{ciphertext}"
decryption_response = requests.get(url_decrypt)

# Extract and display the decrypted plaintext
decrypted_data = decryption_response.json()
plaintext_hex = decrypted_data['plaintext']
plaintext = bytes.fromhex(plaintext_hex).decode('utf-8')

print("Decrypted plaintext:", plaintext)
