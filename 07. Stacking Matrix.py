import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
npa = np.zeros((2,3))
npb = np.ones((2,3))

#stacking matrix
c = np.hstack((a,b))
print(c)
print("-"*50)
c = np.vstack((a,b))
print(c)
print("-"*50)
c = np.vstack((npa,npb))
print(c)
print("-"*50)
c = np.hstack((npa,npb))
print(c)
print("-"*50)

