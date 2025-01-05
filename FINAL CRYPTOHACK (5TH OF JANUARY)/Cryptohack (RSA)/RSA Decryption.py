# Given prime numbers 'p' and 'q', modulus 'N', public exponent 'e', and ciphertext 'c'
prime_p = 857504083339712752489993810777
prime_q = 1029224947942998075080348647219
modulus_N = 882564595536224140639625987659416029426239230804614613279163
public_exponent = 65537
ciphertext = 77578995801157823671636298847186723593814843845525223303932

# Compute Euler's Totient function for 'N' (phi(N) = (p-1)*(q-1))
totient_N = (prime_p - 1) * (prime_q - 1)

# Compute the private exponent 'd' using the modular inverse of 'e' modulo phi(N)
private_exponent = pow(public_exponent, -1, totient_N)

# Decrypt the ciphertext using the private exponent 'd' and modulus 'N'
decrypted_message = pow(ciphertext, private_exponent, modulus_N)

# Output the decrypted message
print("Decrypted message: ", decrypted_message)
