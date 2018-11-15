import numpy as np
# contoh persamaan linear
#y1 = 2*x1 + 3*x2
#y2 = x1 + 2*x2
'''
y = A * x
|y1| |2 3| |x1|
|y2| |1 2| |x2|
'''
A = np.array(([2,3],[1,2]))
#inverse A
A_inv = np.linalg.inv(A)
Y = np.array(([23],[14]))
print("A : \n", A)
print("A_inv : \n", A_inv)
print("Y : \n", Y)
print("-"*50)
# Way 1
print("X = Invers(A) * Y ")
X = np.dot(A_inv,Y)
print(X)
# Way 2
print("Use Builtin Function")
X =np.linalg.solve(A,Y)
print(X)




