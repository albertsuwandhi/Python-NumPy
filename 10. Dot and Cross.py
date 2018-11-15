import numpy as np
#dot --scalar
#a . b = a.b.cos(x)
npa = np.array([1,3])
npb = np.array([2,1])
npc = np.dot(npa,npb)
print("npa : ", npa)
print("npb : ", npb)
print("np.dot(npa,npb) : ", npc)
print("-"*50)

#cross
#a x b = a.b.sin(x)*(vector)
npa = np.array([2,1,0])
npb = np.array([3,2,0])
print("npa : ", npa)
print("npb : ", npb)
npc = print("np.cross(npa,npb) : ", np.cross(npa,npb))
npc = print("np.cross(npa,npb) : ", np.cross(npb,npa))







