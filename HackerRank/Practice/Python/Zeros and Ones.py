import numpy as np
x_2=input().split()
x = map(int,x_2)
value = tuple(x)
# print(x)
# print(x[0])
print(np.zeros(value,dtype=np.int))

print(np.ones(value,dtype=np.int))
# print(np.zeros((int(x[0]),int(x[1]),int(x[2])),dtype=np.int))
# print(np.ones((int(x[0]),int(x[1]),int(x[2])),dtype=np.int))


