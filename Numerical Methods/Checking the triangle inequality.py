import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as pt



def getnorm(x,p):
    return np.sum(np.abs(x)**p, axis=0)**(1/p)

#part a

vec = x + y
a1 = getnorm(vec,1)
a2 = getnorm(vec,2)
a3 = getnorm(vec,5)
a4 = getnorm(vec,0.5)

sum_norm = np.array([a1, a2, a3, a4])

#part b

b1 = getnorm(x,1) + getnorm(y,1)
b2 = getnorm(x,2) + getnorm(y,2)
b3 = getnorm(x,5) + getnorm(y,5)
b4 = getnorm(x,0.5) + getnorm(y,0.5)

norm_sum = np.array([b1,b2,b3,b4])

#part c-f

ptr = np.linspace(0,3.1415926*2,500)
pt_array = np.array([np.cos(ptr),np.sin(ptr)])
scalar = getnorm(pt_array,1)
k = pt_array/scalar

s2 = getnorm(pt_array,2)
k2 = pt_array/s2

s3 = getnorm(pt_array,5)
k3 = pt_array/s3

s4 = getnorm(pt_array, 0.5)
k4 = pt_array/s4


#useless
#for(2) only
#center_x = np.array([np.cos(ptr) + x[0], np.sin(ptr) + x[1]])
#scalar_x = getnorm(center_x,1)
#k_x = center_x/scalar_x
#print(k_x)


#part c

pt.figure()

x1 = getnorm(x,1)
y1 = getnorm(y,1)

c1 = k * x1
c2 = k * y1
c3 = k * a1
c4 = k * b1

pt.plot(c1[0],c1[1], label ='||x||')
pt.plot(c2[0] + x[0],c2[1] + x[1], label = '||y||')
pt.plot(c3[0],c3[1], label = '||x + y||')
pt.plot(c4[0],c4[1], label ='||x|| + ||y||')

pt.legend()

pt.gca().set_aspect("equal")

pt.arrow(0,0,x[0],x[1],length_includes_head=True)
pt.arrow(x[0],x[1],y[0],y[1],length_includes_head=True)
pt.arrow(0,0,(x+y)[0],(x+y)[1],length_includes_head=True)

#pt.legend()

#part d
pt.figure()

x2 = getnorm(x,2)
y2 = getnorm(y,2)

d1 = k2 * x2
d2 = k2 * y2
d3 = k2 * a2
d4 = k2 * b2

pt.plot(d1[0],d1[1], label ='||x||')
pt.plot(d2[0] + x[0],d2[1] + x[1], label ='||y||')
pt.plot(d3[0],d3[1], label ='||x + y||')
pt.plot(d4[0],d4[1], label ='||x|| + ||y||')

pt.gca().set_aspect("equal")

pt.arrow(0,0,x[0],x[1],length_includes_head=True)
pt.arrow(x[0],x[1],y[0],y[1],length_includes_head=True)
pt.arrow(0,0,(x+y)[0],(x+y)[1],length_includes_head=True)

pt.legend()

#part e

pt.figure()

x3 = getnorm(x,5)
y3 = getnorm(y,5)

e1 = k3 * x3
e2 = k3 * y3
e3 = k3 * a3
e4 = k3 * b3

pt.plot(e1[0],e1[1], label ='||x||')
pt.plot(e2[0] +x[0],e2[1]+x[1], label ='||y||')
pt.plot(e3[0],e3[1], label ='||x + y||')
pt.plot(e4[0],e4[1], label ='||x|| + ||y||')

pt.gca().set_aspect("equal")

pt.arrow(0,0,x[0],x[1],length_includes_head=True)
pt.arrow(x[0],x[1],y[0],y[1],length_includes_head=True)
pt.arrow(0,0,(x+y)[0],(x+y)[1],length_includes_head=True)

pt.legend()

#part f

pt.figure()

x4 = getnorm(x,0.5)
y4 = getnorm(y,0.5)

f1 = k4 * x4
f2 = k4 * y4
f3 = k4 * a4
f4 = k4 * b4

pt.plot(f1[0],f1[1], label ='||x||')
pt.plot(f2[0] +x[0],f2[1]+x[1], label ='||y||')
pt.plot(f3[0],f3[1], label ='||x + y||')
pt.plot(f4[0],f4[1], label ='||x|| + ||y||')

pt.gca().set_aspect("equal")

pt.arrow(0,0,x[0],x[1],length_includes_head=True)
pt.arrow(x[0],x[1],y[0],y[1],length_includes_head=True)
pt.arrow(0,0,(x+y)[0],(x+y)[1],length_includes_head=True)

pt.legend()

#part g

print("Triangle inequality is valid when p = 1, 2, and 5. It is not valid when p = 0.5.")




#useless
#for i in range(c.shape[1]):
 #   pt.plot(c[0,i],c[1,i])

#print(sum_norm < norm_sum)
#print(norm_sum)
