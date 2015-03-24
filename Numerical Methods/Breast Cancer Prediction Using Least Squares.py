#  ----------------------------------------------------------
#
#  THIS CODE IS INCOMPLETE! BUT MAY HELP WHEN GETTING STARTED
#
#  ----------------------------------------------------------
import numpy as np
import numpy.linalg as la
import pandas as pd
import matplotlib.pyplot as plt
import scipy.linalg 


def fac(n):
    temp = 1
    for i in range(n):
        temp = temp * (i + 1)
    return temp

def larger(k, n):
    return len(np.where(k > n)[0])

def smaller(k, n):
    return len(np.where(k < n)[0])

tumor = pd.io.parsers.read_csv("breast-cancer-train.dat", header=None, names=labels)
validate = pd.io.parsers.read_csv("breast-cancer-validate.dat", header=None, names=labels)


plt.figure(0)
plt.title("Histgram of Radius")
tumor[labels[4]].hist()
plt.xlabel(labels[4])
plt.ylabel("radius")

plt.figure(1)
tumor[labels[4]].plot()
plt.title("Plot of Radius")
plt.xlabel("radius")
plt.ylabel(labels[4])


def create(A_linear, subset_labels, tumor):
    sub = len(subset_labels)
    cross = fac(sub - 1)
    cols = 2 * sub + cross
    A = np.zeros((A_linear.shape[0], cols))
    count = 0
    for i, col in enumerate(A_linear.T):
        if tumor.columns[2 + i] in subset_labels:
            A[:, count] = col
            A[:, count + 4] = col*col
            count += 1
    count = 0
    col = 2 * sub
    while col < A.shape[1]:
        for idx in range(count + 1, sub):
            A[:, col] = A[:, count]*A[:, idx]
            col += 1
        count += 1
    return(A)

b = tumor["Malignant/Benign"].values
b = (b == "M").astype(np.float64)*2 - 1
v = validate["Malignant/Benign"].values
v = (v == "M").astype(np.float64)*2 - 1

A_linear = np.float64(tumor.values[:, 2:])
B_linear = validate.values[:, 2:]

A_quad = create(A_linear, subset_labels, tumor)
B_quad = create(B_linear, subset_labels, validate)

Q, R = la.qr(A_linear, "complete")
weights_linear = scipy.linalg .solve_triangular(R[:30], Q.T.dot(b)[:30], lower=False)

Q, R = la.qr(A_quad, "complete")
weights_quad = scipy.linalg .solve_triangular(R[:14], Q.T.dot(b)[:14], lower=False)

p_l = B_linear.dot(weights_linear)
p_l[p_l >  0] =  1
p_l[p_l <= 0] = -1


fpl = larger(p_l, v)
fnl = smaller(p_l, v)

p_q = B_quad.dot(weights_quad)
p_q[p_q >  0] =  1
p_q[p_q <= 0] = -1
fpq = larger(p_q, v)
fnq = smaller(p_q, v)

bar_graph(fpl, fnl, fpq, fnq)
