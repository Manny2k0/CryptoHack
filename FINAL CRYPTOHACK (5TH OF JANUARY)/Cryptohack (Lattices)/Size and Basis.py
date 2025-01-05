from math import sqrt

# Tuple of numbers
numbers = (4, 6, 2, 5)

# Calculate the sum of squares of the numbers
total = sum(num ** 2 for num in numbers)

# Calculate the square root of the total
result = sqrt(total)

# Print the result
print(result)  # Output: 9.0