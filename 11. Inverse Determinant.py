import numpy as np
#inverse
#a * a_inverse = Identity Matrix
# tidak semua matrik dapat diinverse --> Matrix Singular
npa = np.array(([1,-1],[1,1]))
print("npa : \n", npa)
npa_inv = np.linalg.inv(npa)
print("inverse npa : \n", npa_inv)
print("npa.npa_inv : \n",np.dot(npa, npa_inv))
#determinant
print("determinant npa : \n", np.linalg.det(npa))
print("determinant npa_inv : \n", np.linalg.det(npa_inv))









