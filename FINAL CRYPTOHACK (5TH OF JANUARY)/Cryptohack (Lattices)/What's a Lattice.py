import numpy as np

"""
Compute the volume of the fundamental domain using the basis vectors vector1 = (6, 2, -3), vector2 = (5, 1, 4), vector3 = (2, 7, 1).
"""
vector1 = np.array([6, 2, -3])
vector2 = np.array([5, 1, 4])
vector3 = np.array([2, 7, 1])

basis_matrix = np.array([vector1, vector2, vector3])

volume = np.math.fabs(np.around(np.linalg.det(basis_matrix), 2))
print("Volume: ", volume)