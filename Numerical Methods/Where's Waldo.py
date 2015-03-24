import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as pt

m = group_image.shape[0]
n = group_image.shape[1]

#get the norm of waldo
w = waldo_image.ravel()
norm_w = la.norm(w,2)

top_left = (0, 0)
smallest = norm_w

a = top_left[0]
b = top_left[1]
c = waldo_image.shape[0]
d = waldo_image.shape[1]

#print(waldo_image.shape)

for i in range(m-c):
    for j in range(n-d):
        #get the snippet of image from group_image
        snippet = group_image[i:i+c,j:j+d]
        #print(snippet.shape)
        #get the difference of waldo and snippet (after reshpae to 1-D)
        diff = waldo_image - snippet
        diff1 = diff.ravel()
        #print(snippet.shape)
        #get the norm
        normw = la.norm(diff1,2)
        #check if it is the smallest
        if normw < smallest:
            smallest = normw
            top_left = (i, j)


group_image = group_image * 0.3
group_image[a:a+c,b:b+d]/0.3


pt.imshow(group_image)
#p = 2
#xs = np.random.randn(m, 1000)
#norm_xs = np.sum(np.abs(xs)**p, axis=0)**(1/p)
#k = xs/norm_xs
#w = waldo_image.dot(k)
#w_norm = np.sum(np.abs(w)**p, axis=0)**(1/p)

#pt.imshow(group_image)
#pt.imshow(waldo_image)
