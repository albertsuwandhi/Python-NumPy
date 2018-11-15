import numpy as np 

# as is array, b is list
a = np.array([1,2,3,4,5])
b = [1,2,3,4,5]

print(type(a))
print(a)
print(type(b))
print(b)

a = a + 1
#below operation (b = b + 1) will raise an error
#b = b + 1
b = b + [1]
print(a)
print(b)