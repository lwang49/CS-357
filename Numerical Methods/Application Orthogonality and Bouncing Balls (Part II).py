import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as pt
from matplotlib.patches import Circle


print("p1: ",p1)
print("p2: ",p2)
print("x0: ",x0)
print("d: ",d)
print("r: ",r)
print("v: ",v)

w = p1 - p2
n = np.array([-w[1],w[0]])
n = n/la.norm(n)
#print(w)
#print(la.norm(n))

t_hit = (n.dot(p1) - r - n.dot(x0))/(v*(n.dot(d)))

positions = np.zeros(shape=(2,30))
print(positions.shape)
print(t_hit)
#t = 29

for i in range(30):
    if i < t_hit:
        xt = x0 + i*v*d
        positions[0][i] = xt[0]
        positions[1][i] = xt[1]
    if i >= t_hit:
        xt2 = x0 + i*v*d - 2*(i-t_hit)*v*(d.dot(n))*n
        positions[0][i] = xt2[0]
        positions[1][i] = xt2[1]
        
#print(positions)
alpha=np.linspace(0,1,100)
#print(alpha)
line = np.empty((2,100,))
for i in range(100):
    temp = alpha[i]*p1 + (1 - alpha[i]) * p2
    line[0][i] = temp[0]
    line[1][i] = temp[1]
    
pt.gca().set_aspect("equal")
pt.plot(line[0],line[1])
pt.gca().set_aspect("equal")
circles(positions[0],positions[1],r)
pt.gca().set_aspect("equal")
