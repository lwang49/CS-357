#  This is incomplete code, but may help when getting started
import numpy as np
import numpy.linalg as la

n = len(streets)
t = 10**(-10)
M, U = m_echelon(flow_matrix.T)
rank = 0
dim_null = 0
while la.norm(U[rank],2) > t:
    rank += 1
dim_null = n - rank

NUT = np.eye(n)[:,rank:]

#  Solve for the null space
nullspace = M.T.dot(NUT)

#  Find eta (i.e. a null space solution),
#+ which closes the street.

for i in range(n):
    if streets[i][0] == closed_street:
        index = i
        
#print(index)
#print(old_street_flow.shape)
#print(nullspace.shape)

eta = np.zeros(old_street_flow.shape)

for i in range(nullspace.shape[0]):
    if nullspace[index][i] != 0:
        eta = nullspace[:,i]
        break
        
#print(eta[index])

#  Find the street flow after the street is closed.

new_street_flow = np.zeros(old_street_flow.shape)

co = -old_street_flow[index]/eta[index]

eta = co*eta

new_street_flow = old_street_flow + eta

#print(new_street_flow)

#  Create dictionaries of original, redirected(eta), and new flow
#+ for plotting.
original_flow = {}
for i, item in enumerate(streets):
    original_flow[item[0]] = old_street_flow[i]

current_flow = {}
for i, item in enumerate(streets):
    current_flow[item[0]] = new_street_flow[i]

redirected_flow = {}
for i, item in enumerate(streets):
    redirected_flow[item[0]] = eta[i]

#print(original_flow)
#print(current_flow)
#print(redirected_flow)


# plot three plots of street network
plot_street_network(streets, intersection_inflow, original_flow, "Original Flow")
plot_street_network(streets, intersection_inflow, redirected_flow, "Redirected Flow")
plot_street_network(streets, intersection_inflow, current_flow, "New Flow")
