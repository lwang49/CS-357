import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as pt

# part(a)

a = p1
b = p2-p1
c = p3-p1

# part(b)

x = p1
y = p2
z = p3

# part(c)

coeffs_a = np.zeros((10, 10, 2))
coeffs_b = np.zeros((10, 10, 3))

alpha = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]).reshape(10, 1)
beta = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]).reshape(1, 10)

coeffs_a[:, :, 0] = alpha
coeffs_b[:, :, 1] = beta

coeffs_b[:, :, 0] = alpha
coeffs_b[:, :, 1] = beta
coeffs_b[:, :, 2] = 1 - alpha - beta

# part(d)

a1 = a.reshape(3,1,1)
b1 = b.reshape(3,1,1)
c1 = c.reshape(3,1,1)
x1 = x.reshape(3,1,1)
y1 = y.reshape(3,1,1)
z1 = z.reshape(3,1,1)

patch_a = a1 + coeffs_a[:, :, 0] * b1 + coeffs_a[:, :, 1] * c1
patch_b = coeffs_b[:, :, 0] * x1 + coeffs_b[:, :, 1] * y1 + coeffs_b[:, :, 2] * z1

fig = pt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot_wireframe(patch_a[0], patch_a[1], patch_a[2], label='part a')
ax.plot_wireframe(patch_b[0], patch_b[1], patch_b[2], label='part b')
ax.set_title('Equivalent planes',fontsize=30)
ax.legend()
