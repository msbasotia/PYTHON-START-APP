import numpy as np

from numpy import pi

a = [0,1,2,3,4,5,6,7,8]

b = np.array(a,dtype = complex)
c = np.array(a,dtype = float)
print(b)
print(c)

d = np.zeros((2,3))
e = np.zeros((2,3),dtype = int)
f = np.zeros((2,3,4),dtype = int)

print(d)
print(e)
print(f)


h = np.ones((2,3))
i = np.ones((2,3),dtype = int)
j = np.ones((2,3,4),dtype = int)

print(h)
print(i)
print(j)


k = np.arange(24)
l = k.reshape(2,3,4)

print(k)
print(l)

m = np.linspace( 0, 2*pi, 10 )
n = np.sin(m)
print(n)


o = np.linspace( 0, 10, 6 )
p = o**2
print(p)
print(o<5)

