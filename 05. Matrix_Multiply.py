import numpy as np 

npa = np.array(([1,2],
                [3,4]))
npb = np.array(([4,7],
                [3,2]))
npc = np.ones([2,2])
npd = np.array(([1,2,3],
                [3,4,5],
                [4,5,6]))
npe = np.array(([1,2],
                [3,4],
                [1,1]))

print("Matrix npa : \n", npa)
print("Matrix npb : \n", npb)
print("Matrix npc : \n", npc)
print("Matrix npd : \n", npd)
print("Matrix npe : \n", npe)
print("-"*60)

#both are matrix multiplication or dot
# Ex : a. b --> number of columns of a must be the same as number of rows b
# 1st way
c1 = np.dot(npa,npb)
# 2nd way
c2 = npa.dot(npc)
# (3,3) . (3,2) --> result = 3 rows x 2 columns
c3 = npd.dot(npe)
print("npa dot npb : \n")
print(c1)
print("-"*60)
print("npa dot npc : \n")
print(c2)
print("-"*60)
print("npd dot npe : \n")
print(c3)
print("-"*60)

