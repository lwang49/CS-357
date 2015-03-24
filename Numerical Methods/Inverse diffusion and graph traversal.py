import numpy as np
import matplotlib.pyplot as pt
import scipy


P,L,U=scipy.linalg.lu(A)
np.set_printoptions(precision=1)


#print(A)

#Find d_8
#A(d_8)=d_9
#A=PLU   PLU(d_8) = d_9    LU(d_8) = (P.T)(d_9)
#L(U(d_8)) = d_9
p_9 = (P.T).dot(d_9)
#print(p_9)
U_8 = scipy.linalg.solve_triangular(L,p_9,lower=True)
d_8 = scipy.linalg.solve_triangular(U,U_8)

#For d_7
p_8 = (P.T).dot(d_8)
U_7 = scipy.linalg.solve_triangular(L,p_8,lower=True)
d_7 = scipy.linalg.solve_triangular(U,U_7)

#For d_6
p_7 = (P.T).dot(d_7)
U_6 = scipy.linalg.solve_triangular(L,p_7,lower=True)
d_6 = scipy.linalg.solve_triangular(U,U_6)

#For d_5
p_6 = (P.T).dot(d_6)
U_5 = scipy.linalg.solve_triangular(L,p_6,lower=True)
d_5 = scipy.linalg.solve_triangular(U,U_5)

#For d_4
p_5 = (P.T).dot(d_5)
U_4 = scipy.linalg.solve_triangular(L,p_5,lower=True)
d_4 = scipy.linalg.solve_triangular(U,U_4)

#For d_3
p_4 = (P.T).dot(d_4)
U_3 = scipy.linalg.solve_triangular(L,p_4,lower=True)
d_3 = scipy.linalg.solve_triangular(U,U_3)

#For d_2
p_3 = (P.T).dot(d_3)
U_2 = scipy.linalg.solve_triangular(L,p_3,lower=True)
d_2 = scipy.linalg.solve_triangular(U,U_2)

#For d_1
p_2 = (P.T).dot(d_2)
U_1 = scipy.linalg.solve_triangular(L,p_2,lower=True)
d_1 = scipy.linalg.solve_triangular(U,U_1)

#For d_0
p_1 = (P.T).dot(d_1)
U_0 = scipy.linalg.solve_triangular(L,p_1,lower=True)
d_0 = scipy.linalg.solve_triangular(U,U_0)

#origin_index
origin_index = np.argmax(d_0)

#Plot four graphs
pt.figure()
pt.title("9 months")
plot_graph(A, d_9)
pt.figure()
pt.title("6 months")
plot_graph(A, d_6)
pt.figure()
pt.title("3 months")
plot_graph(A, d_3)
pt.figure()
pt.title("0 months")
plot_graph(A, d_0)

#Inference
print("The graph infers the distribution of people in different city. The darker the color, more people in that city. For example, in graph 4, all people are in one city and that city has the darkest color, all other city has no color. The graph also shows the tendency of how people move from one city to another, the arrow and the number indicates the trend.")
