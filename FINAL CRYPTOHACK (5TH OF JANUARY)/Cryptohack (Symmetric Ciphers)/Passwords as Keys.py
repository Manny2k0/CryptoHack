from Crypto.Cipher import AES
import hashlib
import requests

# API endpoint for encryption service
API_ENDPOINT = "http://aes.cryptohack.org/passwords_as_keys"

# Fetch the encrypted flag from the API
response = requests.get(f"{API_ENDPOINT}/encrypt_flag")
encrypted_text = response.json()["ciphertext"]
print("Ciphertext:", encrypted_text)

# Read the word list from the file
with open('words.txt') as file:
    word_list = [word.strip() for word in file]

def decrypt_cipher(encrypted, hashed_password):
    """
    Decrypts the given encrypted text using the provided hashed password.
    
    Args:
        encrypted (str): The encrypted text in hexadecimal format.
        hashed_password (str): The hashed password in hexadecimal format.
        
    Returns:
        str: The decrypted text in hexadecimal format.
    """
    encrypted_bytes = bytes.fromhex(encrypted)
    encryption_key = bytes.fromhex(hashed_password)
    aes_cipher = AES.new(encryption_key, AES.MODE_ECB)
    
    try:
        decrypted_data = aes_cipher.decrypt(encrypted_bytes)
    except ValueError as error:
        return {"error": str(error)}
    
    return decrypted_data.hex()

# Iterate through the word list to find the correct password
for word in word_list:
    hashed_password = hashlib.md5(word.encode()).hexdigest()
    decrypted_hex = decrypt_cipher(encrypted_text, hashed_password)
    decrypted_flag = bytes.fromhex(decrypted_hex).decode('utf-8', errors='ignore')
    
    if 'crypto' in decrypted_flag:
        print(decrypted_flag)
        break