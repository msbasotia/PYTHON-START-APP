import numpy as np

a = np.arange(12).reshape(3,4)

print(a)
b = a.sum(axis = 0) #sum along columns
c = a.sum(axis = 1) #sum along rows

print(b)
print(c)

d = a.min(axis = 0) 
e = a.min(axis = 1) 

print(d)
print(e)


f = a.cumsum(axis = 0) 
g = a.cumsum(axis = 1) 

print(f)
print(g)