import numpy as np
import numpy.linalg as la

#print(streets)
#print(n_intersections)
#print(intersection_inflow)

plot_street_network(streets,intersection_inflow,title="initial")

t = 10**(-10)
m = n_intersections
n = len(streets)

flow_matrix = np.zeros((m,n))
#print(flow_matrix.shape)

for i in range(m):
    for j in range(n):
        if streets[j][1] == i:
            flow_matrix[i][j] = -1
        if streets[j][2] == i:
            flow_matrix[i][j] = 1
            
#print(flow_matrix)

M, U = m_echelon(flow_matrix)

#print(U)

rank = 0
dim_null = 0

while la.norm(U[rank],2) > t:
    rank += 1
    
dim_null = n - rank
#print(dim_null)
