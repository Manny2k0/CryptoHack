# Given public exponent 'e', and prime numbers 'p' and 'q'
public_exponent = 65537
prime_p = 857504083339712752489993810777
prime_q = 1029224947942998075080348647219

# Compute Euler's Totient function for 'n = p * q'
totient_n = (prime_p - 1) * (prime_q - 1)

# Compute the private exponent 'd' using modular inverse of 'e' modulo totient of n
private_exponent = pow(public_exponent, -1, totient_n)

# Output the computed private exponent
print(private_exponent)
