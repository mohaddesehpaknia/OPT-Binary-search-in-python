1#Written by Mohaddeseh Paknia
import numpy as np
import math
#input
p = [0.01, 0.02, 0.04, 0.08, 0.16, 0.69]
n = len(p)+1
# The initial value of the cost matrix and k
C = np.zeros((n+1, n))
K = np.zeros((n-1, n-1))
#The main diameter of the cost matrix is ​​equal to the probability of accessing each key
for i in range(1, n):
    C[i, i] = p[i-1]
for i in range(n-1):
    K[i,i] = i+1
#M[i,j] = min(i<=k<=j)[M[i,k-1]+M[k+1,j]]+sigma(k = i to j) p[k]
for l in range(n-2):
    for i in range(1, n-l-1):
        j = i+l+1
        C[i, j] = math.inf
        sp = 0
        for m in range(i,j+1):
            t = C[i, m-1] + C[m+1,j]
            sp += p[m-1] 
            if t < C[i, j]:                
                C[i, j] = t
                K[i-1, j-1] = m
        C[i, j] += sp
#output
print(C)
print(K)
