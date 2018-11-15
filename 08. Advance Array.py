import numpy as np

# matrix with data type
npa = np.array(([1,2,3],[4,5,6]), dtype=int)
npb = np.array(([1,3,3],[4,7,6]), dtype=float)
print(npa)
print(npb)

#matrix  with fromfunction
def kuadrat(baris,kolom):
    return kolom**2
def jumlah(baris,kolom):
    return baris+kolom

hasil = np.fromfunction(kuadrat, (1,8), dtype = int)
print(hasil)
print("-"*50)
hasil = np.fromfunction(jumlah, (3,3), dtype = float)
print(hasil)
print("-"*50)
# from iterable 
iterable = (x*x for x in range (0,5))
#print(iterable)
npc = np.fromiter(iterable, dtype = int)
print(npc)

#multitype array
dtipe1 = [('nama','S255'),('tinggi',int)]
data = [
       ("Mario",100),
       ("Zelda",200),
       ("Luigi",80)]

npd = np.array(data, dtype=dtipe1)
print(npd)
print(npd[1])

dtipe2 = [('nama','S255'),('tinggi',int), ('power', float)]
data = [
       ("Mario",100, 111.5),
       ("Zelda",200, 100.5),
       ("Luigi",80, 80)]
npd = np.array(data, dtype=dtipe2)
print(npd)
print(npd[1])




