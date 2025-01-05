from Crypto.PublicKey import RSA

# Open the public key file and read its content
public_key_file = 'bruce_rsa.pub'

with open(public_key_file, 'r') as key_file:
    # Import the RSA key from the file
    rsa_key = RSA.import_key(key_file.read())
    
    # Print the type of the key and the modulus (n)
    print(f"Key type: {type(rsa_key)}")
    print(f"Modulus (n): {rsa_key.n}")