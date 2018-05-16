import numpy as np
from scipy import sparse
import sympy
A = np.array([0, 0, 0, 1, 1, 0, 0, 1, 1])
M = A.reshape(3, 3)
print(M)
S = sparse.csr_matrix(M)
print(M.size)
print(S.size)