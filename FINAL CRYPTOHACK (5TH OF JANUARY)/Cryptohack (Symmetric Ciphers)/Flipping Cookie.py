import requests
from Crypto.Util.Padding import pad

# URL for the encryption service
ENCRYPTION_URL = 'https://aes.cryptohack.org/ecb_oracle/encrypt/'

def perform_encryption(plaintext):
    """
    Encrypts the given plaintext using the ECB oracle service.
    
    Args:
        plaintext (str or bytes): The plaintext to encrypt.
        
    Returns:
        str: The ciphertext in hexadecimal format.
    """
    # Ensure the input is in byte format
    if isinstance(plaintext, str):
        plaintext = plaintext.encode()

    # Convert plaintext to hexadecimal string
    plaintext_hex = plaintext.hex()

    # Send the encryption request
    response = requests.get(f"{ENCRYPTION_URL}{plaintext_hex}/")

    # Extract and return the ciphertext from the response
    return response.json()['ciphertext']

# Initialize the cipher block with 16 zero bytes
cipher_block = b'\x00' * 16