

import numpy as np

from numpy import pi


print ("--------------")

mat_1 = np.arange(12).reshape(3,4)
print(mat_1)

# how to access each element

for i in range(len(mat_1)):
    for j in range(len(mat_1[i])):
        print(mat_1[i][j])

print ("--------------")        
# Python Lists
a = []

for i in range(8):
    a.append(i)
print(f"The python list is {a}") 
print(f"The numpy matrix is {np.array(a)}") 


print ("--------------")     

#Python 1d list to multi-d list

b = []

print(len(a))

for i in range(0,len(a),2):
    c = []
    for j in range(2):
        c.append(a[i+j])
    b.append(c)

print(f"The original list was {a}")
print(f"The multi-d list is {b}")