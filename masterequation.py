import numpy as np
A = np.array([[0,0,0],[0,0,0],[0,0,0]])

#P = [[0],[1],[0]]

P = np.array([[0, 1, 0]]).T

#print A.shape, P.shape

print A, P, np.matmul(A, P)

deltaP = np.matmul(A, P)

print P*np.e**(deltaP)
