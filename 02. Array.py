import numpy as np 

# Vector
a = np.array([1,2,3,4,5])
b = np.array([1.5, 2.5, 3, 4, 5])
# Vector with range
c = np.arange(1, 10, 2)
d = np.arange(1, 5, 0.5)
# Linear space : Split into parts
e = np.linspace(2, 20, 4)
# Multi dimension array
f = np.array([(1,2,3),(4,5,6)])
# array with zero 
g = np.zeros((3,3))
# array with ones
h = np.ones((2,2))
# identity matrix
i = np.identity(4)
j = np.eye(5)
#print content
print(a)
print("-"*20)
print(b)
print("-"*20)
print(c)
print("-"*20)
print(d)
print("-"*20)
print(e)
print("-"*20)
print(f)
print("-"*20)
print(g)
print("-"*20)
print(h)
print("-"*20)
print(i)
print("-"*20)
print(j)
