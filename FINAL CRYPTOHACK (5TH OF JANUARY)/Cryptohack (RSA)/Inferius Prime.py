from Crypto.Util.number import long_to_bytes

# Given large values for 'n', 'e', ciphertext 'ct', and the prime factors 'p' and 'q'

When you have very big numbers for 'n', 'e', the encrypted message 'ct', and prime factors 'p' and 'q'. It is possible to decrypt the message with these values by first finding out a special number called the private key. Here’s how: First step is calculating something named as Euler’s totient function (φ). For this you use your primes 'p' and 'q'. You do it like below: φ(n) = (p-1) * (q-1) Second step is finding private key ‘d’. It must satisfy equation: d*e ≡ 1 (mod φ(n)). This means that product of ‘d’ times 'e' leaves remainder one when divided by "φ(n)" You can calculate 'd' using method known as Extended Euclidean Algorithm. After getting 'd,' last step involves decrypting original message from ciphertext ('ct'). Formula for decryption looks like this: Original Message = (ct^d) mod n This will give you back original plain text!

modulus_n = 742449129124467073921545687640895127535705902454369756401331

public_exponent = 3

ciphertext = 39207274348578481322317340648475596807303160111338236677373

prime_p = 752708788837165590355094155871

prime_q = 986369682585281993933185289261

# Compute Euler's Totient function for 'n'

totient_n = (prime_p - 1) * (prime_q - 1)

# Compute the modular inverse of 'e' modulo 'phi(n)' to get back private number 'd'

private_exponent = pow(public_exponent, -1, totient_n)

# Decrypt the ciphertext using the private exponent 'd' and modulus 'n'

decrypted_message = pow(ciphertext, private_exponent, modulus_n)

# Convert the decrypted message from a long integer to bytes and print it

print(long_to_bytes(decrypted_message))