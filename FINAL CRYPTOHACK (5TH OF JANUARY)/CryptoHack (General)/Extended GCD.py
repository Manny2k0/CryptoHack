# Initialize the given numbers
num1 = 26513
num2 = 32321

# Ensure num1 is greater than num2
if num1 < num2:
    num1, num2 = num2, num1  # Swap the values if num1 is smaller

# Assign initial values
r1, r2 = num1, num2
s1, s2 = 1, 0
t1, t2 = 0, 1

# Loop to compute the GCD using the extended Euclidean algorithm
while r2 > 0:
    q, r = divmod(r1, r2)  # Compute the quotient and remainder
    r1, r2 = r2, r  # Update r1 and r2 for the next iteration

    # Update s1 and s2 for Bézout's identity
    s1, s2 = s2, s1 - q * s2

    # Update t1 and t2
    t1, t2 = t2, t1 - q * t2

# Print the results: GCD, u and v values for Bézout's identity
print(f"GCD: {r1}, u: {t1}, v: {s1}")
