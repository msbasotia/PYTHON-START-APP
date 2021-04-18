import numpy as np

from numpy import pi

a = [1,2,3,4,5,6,7,8,9]

a1 = np.array(a)
a2 = np.array(a,dtype = complex)

c = []

for i in range(0,7,3):
    b = []
    for j in range(3):
        b.append(a[i+j])
    c.append(b)

print(c)
print(a1)
print(a2)

print(np.ones((3,3),dtype = int))

d = np.linspace(0,10,7)
print(d)


x = np.linspace( 0, 2*pi, 3 )
print(x)