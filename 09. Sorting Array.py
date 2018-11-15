import numpy as np

# 1 row, 6 columns array
#npa =np.floor(np.random.randn(1,8)*10)
# 2 row, 3 columns array
npa =np.floor(np.random.randn(2,3)*10)
print("Nilai npa : \n ", npa)
print("Maksimum dari npa : ", npa.max())
print("Posisi Maksimum dari npa : ", npa.argmax())
print("-"*60)
print("Minimum dari npa : ", npa.min())
print("Posisi minimum dari npa : ", npa.argmin())
print("-"*60)
print("urutan dari npa : \n", np.sort(npa))
# sblm sort
print("Posisi indeks minimum dari npa : \n ", np.argsort(npa))
print("-"*60)
# Sort custom data type
dtipe1 = [('nama','S255'),('tinggi',int), ('power', float)]
data = [
       ("Mario",100, 111.5),
       ("Zelda",90, 100.5),
       ("Luigi",95, 80)]
npb = np.array(data, dtype=dtipe1)
print("isi npb : \n", npb)
print(np.sort(npb, order='nama'))
print(np.sort(npb, order='tinggi'))




