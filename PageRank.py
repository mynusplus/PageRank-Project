import numpy as np
import LinkFinder
from scipy import sparse

#This class is meant to start with an array representing links between website pages and use the pagerank algorithm to
#determine their relative importance.

print(LinkFinder.findLinks())

#This matrix represents the link connections. A 1 in row i and column j means a link from page j to page i. A 0 means
#no link.
linkArray = np.array([[0, 0, 0, 1],
                      [1, 0, 1, 1],
                      [1, 0, 0, 0],
                      [1, 1, 0, 0]])

rowDim = linkArray.shape[0]
colDim = linkArray.shape[1]

linkArray = linkArray.astype(float)

#The link scalars are the number of entries in each column, aka the number of outgoing links from each page.
linkScalars = []
for col in range(colDim):
    for row in range(rowDim):
        if linkArray.item(row, col) != 0:
            if len(linkScalars) == col:
                linkScalars.append(1)
            else:
                linkScalars[col] += 1
print(linkScalars)

#The reciprocal link scalars are just 1 over the link scalars (if link scalar is 0, reciprocal is 0).
reciprocalLinkScalars = []
for scalar in linkScalars:
    if scalar != 0:
        reciprocalLinkScalars.append(1/scalar)
    else:
        reciprocalLinkScalars.append(0)
print(reciprocalLinkScalars)

#Multiplies the matrix columns by their respective reciprocal link scalars.
for col in range(colDim):
    linkArray[:, col] *= reciprocalLinkScalars[col]

print("Matrix A: ")
print(linkArray)

#Creates google matrix G with a value to modify how important/unimportant low page rank sites will be.
linkArray = np.asmatrix(linkArray)
a = .85
G = a*linkArray + (1-a)*(1/rowDim)
print("matrix G:")
print(G)
#S = sparse.csr_matrix(A)

#The estimated matrix to start with in the power_iteration.
b = np.matrix([[1],
               [1],
               [1],
               [1]])


#Stolen from wikipedia: https://en.wikipedia.org/wiki/Power_iteration
#Estimates the eigenvector with highest eigenvalue of the matrix. In this case, that should always be the e-vec with
# e-val of 1. Could fail if the b vector is perpendicular to true answer (I think?)
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


z = power_iteration(linkArray, b, 100)
print("E-vec of B:")
print(z)






# https://scicomp.stackexchange.com/questions/10722/nullspace-algorithm-for-a-sparse-matrix