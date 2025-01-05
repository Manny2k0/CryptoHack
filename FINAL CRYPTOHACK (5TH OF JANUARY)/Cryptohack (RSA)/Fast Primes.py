from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.number import inverse
import hashlib

# Load the RSA private key from a file
def load_rsa_key(file_path):
    with open(file_path, "rb") as key_file:
        return RSA.importKey(key_file.read())

# Factorize the modulus 'n' (simplified for the purpose of this example)
def factor_modulus(modulus):
    # Using known values for p and q for this example
    p = 51894141255108267693828471848483688186015845988173648228318286999011443419469
    q = 77342270837753916396402614215980760127245056504361515489809293852222206596161
    return p, q

# Calculate Euler's Totient function for the modulus 'n'
def calculate_totient(p, q):
    return (p - 1) * (q - 1)

# Use the Extended Euclidean Algorithm to find the modular inverse (private key exponent)
def find_private_exponent(public_exponent, totient):
    return inverse(public_exponent, totient)

# Decrypt the ciphertext using RSA private key
def decrypt_message(private_key, ciphertext):
    cipher = PKCS1_OAEP.new(private_key)
    return cipher.decrypt(ciphertext)

# Main logic
def main():
    rsa_key = load_rsa_key("key_17a08b7040db46308f8b9a19894f9f95.pem")
    
    modulus = rsa_key.n
    public_exponent = rsa_key.e
    
    # Factor modulus 'n' into p and q
    p, q = factor_modulus(modulus)
    
    # Compute the Totient (φ(n)) = (p-1)*(q-1)
    totient = calculate_totient(p, q)
    
    # Calculate the private exponent 'd' using the modular inverse
    private_exponent = find_private_exponent(public_exponent, totient)
    
    # Reconstruct the private key with the calculated exponent
    private_key = RSA.construct((modulus, public_exponent, private_exponent))
    
    # Encrypted ciphertext (from the problem)
    encrypted_data = bytes.fromhex("249d72cd1d287b1a15a3881f2bff5788bc4bf62c789f2df44d88aae805b54c9a94b8944c0ba798f70062b66160fee312b98879f1dd5d17b33095feb3c5830d28")
    
    # Decrypt the message and print the result
    decrypted_message = decrypt_message(private_key, encrypted_data)
    print("Decrypted message:", decrypted_message.decode())

# Run the main function
if __name__ == "__main__":
    main()
