import numpy as np

x = -1
y = 1
z = -1
# Create T matrix
T = np.array([[1, x, y, z], 
              [x, 1, z, y], 
              [y.conjugate(), z.conjugate(), 1, x.conjugate()], 
              [z.conjugate(), y.conjugate(), x.conjugate(), 1]])

# Calculate eigenvalues of T
eigenvalues = np.linalg.eigvals(T)

print("Matrix T:")
print(T)

print("\nEigenvalues of T:")
print(eigenvalues)
