import numpy as np
from scipy import sparse

A = np.matrix([[0, 0, 0, 1],
              [1, 0, 1, 1],
              [1, 0, 0, 0],
               [1, 1, 0, 0]])
K = []
for i in range(A.shape[1]):
    for j in range(A.shape[0]):
        if A.item(j, i) != 0:
            if len(K) == i:
                K.append(1)
            else:
                K[i] += 1
print(K)
J = []
for i in K:
    if i != 0:
        J.append(1/i)
    else:
        J.append(0)
print(J)

L = [[0, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 0, 0]]

T = np.matrix([[x * J[0] for x in L[0]],
               [x * J[1] for x in L[1]],
               [x * J[2] for x in L[2]],
               [x * J[3] for x in L[3]]])
B = T.T
print('matrix B:')
print(B)

a = .85
n = B.shape[0]
G = a*B + (1-a)*(1/n)
print("matrix G:")
print(G)
#S = sparse.csr_matrix(A)

b = np.matrix([[1],
               [1],
               [1],
               [1]])


#Stolen from wikipedia:
def power_iteration(M, b_k, num_simulations):
    # Ideally choose a random vector
    # To decrease the chance that our vector
    # Is orthogonal to the eigenvector

    #b_k = np.random.rand(M.shape[0])

    for _ in range(num_simulations):
        # calculate the matrix-by-vector product Ab
        b_k1 = M * b_k
        #print("b_k1:")
        #print(b_k1)
        # calculate the norm
        b_k1_norm = np.linalg.norm(b_k1)
        #print("b_k1_norm:")
        #print(b_k1_norm)
        # re normalize the vector
        b_k = b_k1 / b_k1_norm
        #print("b_k:")
        #print(b_k)
    return b_k


z = power_iteration(B, b, 100)
print("E-vec of B:")
print(z)





# https://scicomp.stackexchange.com/questions/10722/nullspace-algorithm-for-a-sparse-matrix