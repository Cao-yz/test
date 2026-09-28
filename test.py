import sys
import numpy as np

print("Python executable:")
print(sys.executable)

print("\nNumPy version:")
print(np.__version__)

A = np.array([
    [1, 2],
    [3, 4],
])

print("\nEigenvalues:")
print(np.linalg.eigvals(A))