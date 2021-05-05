## No 1

def luas_persegi():
    print ('program mencari luas persegi')
    print ('--------------------------------------------')
    s= float(input ('panjang sisi : '))
    luasp= s*s
    print (' ' )
    print ('luas persegi = sisi x sisi. Maka luasnya = ' , luasp , 'satuan luas')

def luas_lingkaran():
    print (' program mencari luas lingkaran ')
    print ('--------------------------------------------')
    r = float(input('masukkan jari-jari lingkaran : '))
    luas = 22/7*r*r
    print ('')
    print ('luas lingkaran = 22/7 x r x r. Maka luasnya = ' , luas , 'satuan luas')
    
def luas_segitiga():
    print ('--------------------------------------------')
    print ('program mencari luas segitiga' )
    print ('--------------------------------------------')
    a= float(input('masukkan alas segitiga : '))
    t= float(input('masukkan tinggi segitiga :'))
    luas =0.5*a*t
    print (' ' )
    print ('luas segitiga = 1/2 x alas x tinggi. Maka luasnya = ' , luas, 'satuan luas')
   
def luas_bk():
    print ('--------------------------------------------')
    print (' program mencari luas belah ketupat ')
    print ('--------------------------------------------')
    x= float(input('masukkan diagonal 1 : '))
    y= float(input('masukkan diagonal 2 : ' ))
    luas = 0.5*x*y
    print ('')
    print ('luas belah ketupat = 1/2 x diagonal1 x diagonal2. Maka luasnya = ', luas, 'satuan luas')


##2
#a
X = [[12,7]]
Y = [[5,8,1],
    [6,7,3]]
result = [[0,0,0]]

for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

##print("Matriks A",X)
##print("Matriks B",Y)
##print("Hasilnya : ")
##for r in result:
##   print(r)

##b
matrix = []

for i in range(7):
    a =[]
    for j in range(7):
        if j == i:
            a.append(int(1))
        else:
            a.append(int(0))
    matrix.append(a)
##print("Matriks identitas ordo 7x7")
##for i in range(7):
##    for j in range(7):
##        print(matrix[i][j], end = " ")
##    print()

## 3
class Manusia():
    def __init__(self, nama, umur, kulit):
        self.nama = nama
        self.umur = umur
        self.kulit = kulit
    def __str__(self):
        return str(self.nama)+" "+str(self.umur)+" "+str(self.kulit)

data1 = Manusia("Edy",20,"Kuning Langsat")
data2 = Manusia("Susilo",20,"Putih")
data3 = Manusia("Rahmat",23,"Putih")
data4 = Manusia("Agung",24,"Sawo Matang")
data5 = Manusia("Asep",28,"Putih")
data6 = Manusia("Cahyo",18,"Kuning Langsat")
data7 = Manusia("Farhan",18,"Kuning Langsat")
data8 = Manusia("Nur",19,"Putih")
data9 = Manusia("Fatah",14,"Kuning Langsat")
data10 = Manusia("Iqbal",17,"Sawo Matang")

data = [data1,data2,data3,data4,data5,data6,data7,data8,data9,data10]
def dataNama(i):
    for i in data:
        print(i.nama)
def dataUmur(i):
    for i in data:
        print(i.umur)
def warnaKulit(i):
    for i in data:
        print(i.kulit)

##4
def cari(a):
    print("Daftar orang berkulit " + a)
    for i in range(len(data)):
        if a == data[i].kulit:
            print(data[i].nama)
    
#5
def urutkanUmur(data):
    for x in range(len(data)):
        mins = 0
        for y in range(-1,len(data)):
            minimal = data[mins].umur
            if minimal < data[y].umur:
                mins = y
            data[mins],data[x] = data[x],data[mins]
    return data
print("Data Sebelum Diurutkan")
for i in data:
    print(i.umur, i.nama)

print("Data Sesudah Diurutkan")
urutkanUmur(data)
for i in data:
    print(i.umur, i.nama)
