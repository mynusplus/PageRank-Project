import numpy as np
import LinkFinder
from scipy import sparse

# This class is meant to start with an array representing links between website pages and use the pagerank algorithm to
# determine their relative importance.

# Gets page link information from LinkFinder
linkNums = LinkFinder.findLinks()

# Defines dim value for later, is the dimension of the array we are making. Same for columns and rows since matrix is
# square.
dim = len(linkNums)

# Makes zero array of the required size.
linkArray = np.zeros((len(linkNums), len(linkNums)), dtype=float)

# Sets entries of matrix to construct a matrix that represents link connections.  A 1 in row i and column j means a link
# from page j to page i. A 0 means no link.
for col in linkNums:
    for row in linkNums[col]:
        linkArray[row, col] = 1

# The link scalars are the number of entries in each column, aka the number of outgoing links from each page.
linkScalars = []
for col in range(dim):
    for row in range(dim):
        if linkArray.item(row, col) != 0:
            if len(linkScalars) == col:
                linkScalars.append(1)
            else:
                linkScalars[col] += 1
        else:
            if len(linkScalars) == col:
                linkScalars.append(0)

# The reciprocal link scalars are just 1 over the link scalars (if link scalar is 0, reciprocal is 0).
reciprocalLinkScalars = []
for scalar in linkScalars:
    if scalar != 0:
        reciprocalLinkScalars.append(1/scalar)
    else:
        reciprocalLinkScalars.append(0)

# Multiplies the matrix columns by their respective reciprocal link scalars.
for col in range(dim):
    linkArray[:, col] *= reciprocalLinkScalars[col]

print("Matrix A: ")
print(linkArray)

# Creates google matrix with a value to modify how important/unimportant low page rank sites will be. Google used
# a = .85, so that's what I'm doing.
linkMatrix = np.asmatrix(linkArray)
a = .85
googleMatrix = a*linkMatrix + (1-a)*(1/dim)
print("matrix googleMatrix:")
print(googleMatrix)

# Stolen from wikipedia: https://en.wikipedia.org/wiki/Power_iteration
# Estimates the eigenvector with highest eigenvalue of the matrix. In this case, that should always be the e-vec with
# e-val of 1. Could fail if the b_k vector is perpendicular to true answer (I think?)
def power_iteration(M, num_simulations):
    # Ideally choose a random vector
    # To decrease the chance that our vector
    # Is orthogonal to the eigenvector

    b_k = np.random.rand(dim, 1)

    for _ in range(num_simulations):
        # calculate the matrix-by-vector product Ab
        b_k1 = M * b_k
        # calculate the norm
        b_k1_norm = np.linalg.norm(b_k1)
        # re normalize the vector
        b_k = b_k1 / b_k1_norm

    return b_k


evec = power_iteration(linkMatrix, 50)
print("E-vec of linkMatrix:")
print(evec)

evecG = power_iteration(googleMatrix, 50)
print("E-vec of googleMatrix:")
print(evecG)






# https://scicomp.stackexchange.com/questions/10722/nullspace-algorithm-for-a-sparse-matrix