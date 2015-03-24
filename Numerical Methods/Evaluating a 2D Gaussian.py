import numpy as np
import numpy.linalg as la
import matplotlib.pyplot 


m = len(x)
n = len(y)

x1 = np.zeros((2, m, n))
x1[0] = x.reshape(-1,1)
x1[1] = y

x1 = x1 - mu.reshape(2,1,1)


Sigma_inv_x_vec = np.tensordot(la.inv(covariance_mat), x1, 1)
scalar = (x1[0] * Sigma_inv_x_vec[0]
          + x1[1] * Sigma_inv_x_vec[1])

gaussian = np.exp(-1/2*scalar)


matplotlib.pyplot.imshow(gaussian)
