import math
import numpy as np

# Function to apply the Gram-Schmidt process to a set of vectors
def gram_schmidt_process(matrix):
    rows, cols = len(matrix), len(matrix[0])
    orthogonal_matrix = np.zeros((rows, cols))
    
    # Initialize the first vector
    orthogonal_matrix[0, :] = matrix[0, :]
    
    # Apply the Gram-Schmidt orthogonalization process
    for i in range(1, rows):
        orthogonal_matrix[i, :] = matrix[i, :]
        for j in range(i):
            # Project the current vector onto the previous ones and subtract
            projection_factor = orthogonal_matrix[j, :].dot(orthogonal_matrix[i, :]) / orthogonal_matrix[j, :].dot(orthogonal_matrix[j, :])
            orthogonal_matrix[i, :] = orthogonal_matrix[i, :] - projection_factor * orthogonal_matrix[j, :]
    
    return orthogonal_matrix

# Example basis vectors for the transformation
basis_vectors = np.array(
    [
        np.array((4, 1, 3, -1)),
        np.array((2, 1, -3, 4)),
        np.array((1, 0, -2, 7)),
        np.array((6, 2, 9, -5)),
    ]
)

# Perform the Gram-Schmidt process to get an orthogonal basis
orthogonal_basis = gram_schmidt_process(basis_vectors)

# Print the orthogonal matrix
print(orthogonal_basis)

# Print a specific element of the orthogonal matrix with 5 decimal places
print("{0:.5f}".format(orthogonal_basis[3][1]))
