import numpy as np
import numpy.linalg as la

#A = np.array([[3,4,5],[6,7,8],[9,10,11]])

n = A.shape[0]

E = np.zeros([n-1,n,n])
M = np.zeros([n-1,n,n])

U = A.copy()

#L = np.zeros([n,n])
#U = np.zeros([n,n])

for i in range(n-1):
    E[i] = np.eye(n)
    M[i] = np.eye(n)

for i in range(n-1):
    for j in range(i+1,n):
        M[i,j,i]  = -U[j,i]/U[i,i]
        E[i,j,i]  =  U[j,i]/U[i,i]
    U = M[i].dot(U)

L = E[n-2]


for i in range(1,n-1):
    L = E[n-2-i].dot(L)
    
print(L.dot(U))
