import numpy
import math
from numpy import matrix
from numpy import linalg

def modMatInv(A,p):       # Finds the inverse of matrix A mod p
    n = len(A)
    A = matrix(A)
    adj=numpy.zeros(shape=(n,n))
    for i in range(0,n):
        for j in range(0,n):
            adj[i][j]=((-1)**(i+j)*int(round(linalg.det(minor(A,j,i)))))%p
    return (modInv(int(round(linalg.det(A))),p)*adj)%p


def modInv(a,p):          # Finds the inverse of a mod p, if it exists
    for i in range(1,p):
        if (i*a)%p==1:
            return i
    raise ValueError(str(a)+" has no inverse mod "+str(p))


def minor(A, i, j):    # Return matrix A with the ith row and jth column deleted
    A = numpy.array(A)
    minor = numpy.zeros(shape=(len(A)-1, len(A)-1))
    p = 0
    for s in range(0,len(minor)):
        if p == i:
            p += 1
        q = 0
        for t in range(0,len(minor)):
            if q == j:
                q += 1
            minor[s][t] = A[p][q]
            q += 1
        p += 1
    return minor