import requests
import json
from binascii import hexlify, unhexlify
from pwn import xor

BASE_URL = "http://aes.cryptohack.org/lazy_cbc"

def encrypt_message(base_url, message):
    """
    Encrypts the given message using the provided URL.
    
    Args:
        base_url (str): The base URL for the encryption service.
        message (str): The message to encrypt.
        
    Returns:
        dict: The JSON response from the encryption service.
    """
    url = f"{base_url}/encrypt/{hexlify(message.encode()).decode()}/"
    response = requests.get(url)
    return response.json()

def receive_response(base_url, cipher):
    """
    Receives the response for the given cipher from the provided URL.
    
    Args:
        base_url (str): The base URL for the encryption service.
        cipher (str): The cipher text to send.
        
    Returns:
        dict: The JSON response from the encryption service.
    """
    url = f"{base_url}/receive/{cipher}/"
    response = requests.get(url)
    return response.json()

def get_flag(base_url, secret_key):
    """
    Retrieves the flag using the provided secret key.
    
    Args:
        base_url (str): The base URL for the encryption service.
        secret_key (str): The secret key to use.
        
    Returns:
        str: The plaintext flag.
    """
    url = f"{base_url}/get_flag/{secret_key}/"
    response = requests.get(url)
    return response.json()['plaintext']

# Initial text to encrypt
initial_text = 'a' * 48

# Encrypt the initial text
encrypted = encrypt_message(BASE_URL, initial_text)['ciphertext']

# Manipulate the encrypted text to get the error message
error_message = receive_response(BASE_URL, encrypted[:32] + '0' * 32 + encrypted[:32])['error'].split(':')[1].strip()

# Derive the key from the error message
derived_key = xor(unhexlify(error_message[:32]), bytes.fromhex(error_message[64:]))

# Retrieve and print the flag
flag = unhexlify(get_flag(BASE_URL, derived_key.hex())).decode()
print(flag)