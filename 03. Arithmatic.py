import numpy as np 

a = [1,2,3,4,5]
b = [2,4,6,8,10]
npa = np.array([1,2,3,4,5])
npb = np.array([2,4,7,9,10])
# List Operation
print(a+b)
print("-"*60)
# -, *, and / won't work on list
#print(a-b)
#print(a*b)
#print(a/b)
# Array Operation : All Operation are elementwise operation
print(npa+npb)
print("-"*60)
print(npa-npb)
print("-"*60)
print(npa*npb)
print("-"*60)
print(npa/npb)
print("-"*60)
print(npa**2)
print("-"*60)



