import numpy as np

s = 0
result = []
bench = shape[0]

for k in A:
    while s < k:
        result.append(0)
        s = s + 1
    s = s + 1    
    sum = 0
    for h in A[k]:
        sum = sum + x[h] * A[k][h]
    result.append(sum)   
    
while s < bench:
    result.append(0)
    s = s + 1

Ax = np.array(result)
print(Ax)
