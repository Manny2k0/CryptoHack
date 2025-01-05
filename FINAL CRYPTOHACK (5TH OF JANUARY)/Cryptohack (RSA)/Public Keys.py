# Base, exponent, and modulus for the modular exponentiation operation

base_value = 12

exponent_value = 65537

modulus_value = 17 * 23  # The modulus is the product of two primes

# Perform modular exponentiation: (base^exponent) % modulus

result = pow(base_value, exponent_value, modulus_value)

# Output the result of the modular exponentiation

print(result)