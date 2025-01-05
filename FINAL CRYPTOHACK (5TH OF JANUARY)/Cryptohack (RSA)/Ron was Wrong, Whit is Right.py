from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.number import *
import os

# Function to gather keys from the specified directory
def collect_keys(path):
    key_list = []
    for idx in range(50):
        pem_file = open(f"{path}/{idx + 1}.pem").read()
        rsa_key = RSA.importKey(pem_file)
        key_list.append((idx, rsa_key.n, rsa_key.e))
    return key_list

# Collecting the keys from the directory
keys = collect_keys("keys_and_messages")

# Initialize product of n values (modulus of each key)
product_of_n = 1
for idx, n, e in keys:
    product_of_n *= n

# Try to find common factors and decrypt the message
for idx, n, e in keys:
    # Calculate the GCD of the current n and the product of all other n's
    common_gcd = GCD(n, product_of_n // n)
    
    # If the common GCD is not 1, it means we found the factorization
    if idx == 20 and common_gcd != 1:
        factor_p = common_gcd
        factor_q = n // factor_p
        
        # Compute Euler's Totient function (phi)
        phi_n = (factor_p - 1) * (factor_q - 1)
        
        # Calculate the private exponent d
        private_exponent = inverse(e, phi_n)
        
        # Load the ciphertext from the corresponding file
        ciphertext = bytes.fromhex(open(f"keys_and_messages/{idx + 1}.ciphertext").read())
        
        # Construct the RSA key with the private exponent
        rsa_key = RSA.construct((n, e, private_exponent))
        
        # Decrypt the ciphertext using PKCS1_OAEP
        cipher = PKCS1_OAEP.new(rsa_key)
        
        # Print the decrypted message
        print(cipher.decrypt(ciphertext))
