import numpy as np 

a = np.arange(10)**2
b = np.array(([1,2,3],
                [3,4,5],
                [4,5,6]))
print(a)
print("-"*40)
#indexing
print("Elemen ke {} dari a adalah : {}".format(1,a[0]))
print("Elemen ke {} dari a adalah : {}".format(5,a[4]))
#slicing
print("Elemen ke 1 s/d 6 dari a adalah : {}".format(a[0:6]))
print("Elemen ke 4 s/d akhir dari a adalah : {}".format(a[3:]))
print("Elemen awal s/d 5 dari a adalah : {}".format(a[:5]))
print("Elemen baris 1 dari b adalah : {}".format(b[0,0:]))
print("Elemen baris 2 kolom 2 dan 3 dari b adalah : {}".format(b[1,1:]))
#iteration
for i in a:
    print(f"Value : {i}")


