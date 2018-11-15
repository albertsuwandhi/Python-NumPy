import numpy as np
a = np.array(([1,2,3],
             [4,5,6]))
print("Matrix a punya dimensi : {}".format(a.shape))
print (a)
print("-"*60)
#Transpose - Return value only, don't change a
print("Transpose : \n {} ".format(a.T))
print("Transpose : \n {} ".format(a.transpose()))
print("Transpose : \n {} ".format(np.transpose(a)))
print("-"*60)
#Flatten - Return value only, don't change a
print("Flatten : \n {} ".format(a.ravel()))
print("Flatten : \n {} ".format(np.ravel(a)))
print("-"*60)
#reshape - Return value only, don't change a
print("Resize : \n {} ".format(a.reshape(3,2)))
print("Resize : \n {} ".format(np.reshape(6,1)))
print("-"*60)
#resize
print("Resize Matrix a")
a.resize(3,2)
print(a) 
