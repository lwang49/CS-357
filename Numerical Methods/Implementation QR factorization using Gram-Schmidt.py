import numpy as np
import numpy.linalg as la

L = len(As)
#print(As[0].shape,As[1].shape)
Qs = []
Rs = []

for i in range(L):
    #print(As[i].shape)
    if As[i].shape[0]==As[i].shape[1]:
        Q = np.zeros(As[i].shape)
        R = np.zeros((As[i].shape[0], As[i].shape[0]))
    else:
        Q = np.zeros((As[i].shape[0],As[i].shape[1]))
        R = np.zeros((As[i].shape[1], As[i].shape[1]))
    Qs.append(Q)
    Rs.append(R)
    #print("Q ",i, ": ",Q.shape)
    #print("R ",i, ": ",R.shape)

    

def qr_by_gram_schmidt(As):
    #go over every thing in the list
    for i in range(L):
        #create Q same shpae as every element of list As
        #Qs[i] = np.zeros(As[i].shape)
        #Rs[i] = np.zeros((As[i].shape[0], As[i].shape[0]))
        #Get Q & R
        for k in range(As[i].shape[1]):
            q = As[i][:, k]
            for j in range(k):
                #Q[:, j] = q/la.norm(q)
                coeff = np.dot(q,Qs[i][:,j])
                Rs[i][j,k]=coeff
                q = q - np.dot(q, Qs[i][:,j])*Qs[i][:,j]
                
            Rs[i][k,k] = la.norm(q)
            Qs[i][:, k] = q/la.norm(q)
    
qr_by_gram_schmidt(As)
#print(Rs[2].shape,Rs[3].shape,Rs[4].shape)
#print(len(Qs))
