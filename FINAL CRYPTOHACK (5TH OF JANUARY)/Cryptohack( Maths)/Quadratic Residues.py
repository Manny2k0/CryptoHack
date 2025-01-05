# Define the prime number p and the list of integers
prime_p = 29
integers_list = [14, 6, 11]

# Find the quadratic residues modulo p that are in the integers_list
quadratic_residues = [num for num in range(prime_p) if pow(num, 2, prime_p) in integers_list]

# Print the smallest quadratic residue as the flag
flag = min(quadratic_residues) if quadratic_residues else None
print(flag)
