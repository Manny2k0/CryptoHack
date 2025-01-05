import numpy as np

# Function to compute the dot product of two vectors manually (without using numpy)
def custom_dot_product(vec1, vec2):
    return np.sum([a * b for a, b in zip(vec1, vec2)])

# Function to perform the Gauss reduction process (for finding a pair of vectors)
def gauss_reduction(vec1, vec2):
    while True:
        # Swap vectors if the dot product of the first vector is larger than the second
        if custom_dot_product(vec1, vec1) > custom_dot_product(vec2, vec2):
            vec1, vec2 = vec2, vec1
        
        # Calculate the scaling factor m to reduce the second vector
        scaling_factor = custom_dot_product(vec1, vec2) // custom_dot_product(vec1, vec1)
        
        # If scaling factor is 0, return the vectors
        if scaling_factor == 0:
            return vec1, vec2
        
        # Update the second vector using the scaling factor
        vec2 = [v2x - scaling_factor * v1x for v1x, v2x in zip(vec1, vec2)]

# Example vectors
vector_u = [87502093, 123094980]
vector_v = [846835985, 9834798552]

# Perform the Gauss reduction on the vectors
vector_u, vector_v = gauss_reduction(vector_u, vector_v)

# Calculate and print the dot product of the resulting vectors
print(custom_dot_product(vector_u, vector_v))
