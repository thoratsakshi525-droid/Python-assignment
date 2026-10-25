
import numpy as np

# Define matrices
A = np.array([[2, 1], [1, 3]])
B = np.array([5, 6])

# Solve matrix equation AX = B
X = np.linalg.solve(A, B)
print("Solution of AX = B:")
print(X)

# Inverse of matrix
print("\nInverse of Matrix:")
print(np.linalg.inv(A))

# Transpose of matrix
print("\nTranspose of Matrix:")
print(A.T)

# Eigenvalues and eigenvectors
values, vectors = np.linalg.eig(A)
print("\nEigenvalues:")
print(values)

print("\nEigenvectors:")
print(vectors)
