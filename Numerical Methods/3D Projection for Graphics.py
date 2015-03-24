import numpy as np
import matplotlib.pyplot as pt

L = len(angles_and_distances)
M = triangles.shape[0]
n = np.zeros([L,3])
P = np.zeros([L,3,3])
B = np.zeros([3,2])
plane_span = np.zeros([L,3,2])
I = np.zeros([L,M,3,4]) 
I_screen = np.zeros([L,M,2,4])
distance = np.zeros([L,M,4])
I_persp = np.zeros([L,M,2,4]) 

for i in range(L):
    t, d = angles_and_distances[i]
    n[i,:] = [-np.cos(t), -np.sin(t),0]
    temp = np.array([[-np.sin(t), np.cos(t), 0],[0, 0, 1],])
    plane_span[i,:,:] = temp.T
    Q = plane_span[i,:,:]
    P[i,:,:] = Q.dot(Q.T)
    for j in range(M):
        I[i,j,:,:] = P[i,:,:].dot(triangles[j,:,:])
        I_screen[i,j,:,:] = Q.T.dot(I[i,j,:,:])
        distance[i,j,:] = abs(-d - n[i,:].dot(triangles[j,:,:]))
        I_persp[i,j,:,:] = I_screen[i,j,:,:] /distance[i,j,:]
        x = I_persp[i,j,0,:]
        y = I_persp[i,j,1,:]
        pt.plot(x, y)
    pt.figure(i)
