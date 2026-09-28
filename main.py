import numpy as np

H = np.array([
    [1, 0],
    [0, -1]
])

eigvals = np.linalg.eigvalsh(H)
print("Eigenvalues:", eigvals)