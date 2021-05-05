####NO 1
##class Koran():
##    def __init__ (self, parameter):
##        self.parameter = parameter.split(';')
##        self.nama = self.parameter[0]
##        self.kota = self.parameter[1]
##        self.kodepos = self.parameter[2]
##        self.url = self.parameter[3]
##        self.berdiri = self.parameter[4]
##    def __str__(self):
##        return str(self.nama+" - "+self.url)
####
##
####NO 2
##krn = """Nama;Kota;KodePos;URL;Berdiri
##Republika;Jakarta;12150;republika.co.id;1995
##Kompas;Jakarta;54678;kompastv.com;1986
##Koran Jakarta;Jakarta;87658;koranjakarta.com;2008
##Jawa Pos;Surabaya;89769;jawapos.com;1949
##Koran Tempo;Bandung;56743;koran.tempo.co;2001
##Koran Sindo;Jakarta;10340;koran-sindo.com;2005
##Media Indonesia;Jakarta;11520;mediaindonesia.com;1970
##Rakyat Merdeka;Jakarta;56347;rmco.id;1997
##Suara Karya;Semarang;67895;suarakarya.id;1971
##SoloPos;Surakarta;54778;solopos.com;1997
##Suara Merdeka;Semarang;98625;suramerdeka.com;1950
##"""

####NO 3
##class Teks(object):
##    def __init__(self, n):
##        self._internal = n * [None]     
##    def getitem(self, key):
##        if 1 <= key < len(self._internal):
##            return self._internal[key]
##        else:
##            raise ValueError("Tidak Dapat Disimpan")
##        
##    def setitem(self, key, value):
##        if 1 <= key < len(self._internal):
##            self._internal[key]=value
##        else:
##            raise ValueError("Tidak Dapat Disimpan")

####        
####NO 4
##class Simpan():
##    def __init__(self,parameter):
##        self.jj = parameter.split('\n')
##        self.baca = []
##        for i in range(0,10):
##            self.baca.append(Koran(self.jj[i]))
#### No 5           
##    def lihat(self, x):
##        print(self.baca[x].nama + ',' + self.baca[x].kota + ',' + self.baca[x].kodepos)
## No 6
krn = """Nama;Kota;KodePos;URL;Berdiri
Republika;Jakarta;12150;republika.co.id;1995
Kompas;Jakarta;54678;kompastv.com;1986
Koran Jakarta;Jakarta;87658;koranjakarta.com;2008
Jawa Pos;Surabaya;89769;jawapos.com;1949
Koran Tempo;Bandung;56743;koran.tempo.co;2001
Koran Sindo;Jakarta;10340;koran-sindo.com;2005
Media Indonesia;Jakarta;11520;mediaindonesia.com;1970
Rakyat Merdeka;Jakarta;56347;rmco.id;1997
Suara Karya;Semarang;67895;suarakarya.id;1971
SoloPos;Surakarta;54778;solopos.com;1997
Suara Merdeka;Semarang;98625;suramerdeka.com;1950
"""
class Koran():
    def __init__ (self, parameter):
        self.parameter = parameter.split(';')
        self.nama = self.parameter[0]
        self.kota = self.parameter[1]
        self.kodepos = self.parameter[2]
        self.url = self.parameter[3]
        self.berdiri = self.parameter[4]
    def __str__(self):
        return str(self.parameter)
        return str(self.nama+" - "+self.url)
class Teks(object):
    def __init__(self, n):
        self._internal = n * [None]     
    def getitem(self, key):
        if 1 <= key < len(self._internal):
            return self._internal[key]
        else:
            raise ValueError("Tidak Dapat Disimpan")
        
    def setitem(self, key, value):
        if 1 <= key < len(self._internal):
            self._internal[key]=value
        else:
            raise ValueError("Tidak Dapat Disimpan")
class Simpan():
    def __init__(self,parameter):
        self.jj = parameter.split('\n')
        self.baca = []
        for i in range(0,10):
            self.baca.append(Koran(self.jj[i]))        
    def lihat(self, x):
        print(self.baca[x].nama + ',' + self.baca[x].kota + ',' + self.baca[x].kodepos)

## Membuat Array
baca = Teks(12)
## Memanggil methos Simpan
simpan = Simpan(krn)
## Memanggil Method Lihat
simpan.lihat(6)
## Menampilkan Item ke-6
print(simpan.baca[6])
# Python3 program to implement Binary 
# Search for strings
  
# Returns index of x if it is present
# in arr[], else return -1
def cari(x):
    simpan = Simpan(krn)
    arr = simpan.baca
    l = 0
    r = len(arr)
    print(arr)
    while (l <= r):
        mid = l + ((r - l) // 2)
##        print(arr[mid].kodepos)
        if arr[mid].kodepos == x:
            return (arr[mid].nama)
        elif x < arr[mid].kodepos:
            r = mid - 1
        else:
            r = mid + 1
    return False

##        res = (x == arr[m])
##  
##        # Check if x is present at mid
##        if (res == 0):
##            return m - 1
##  
##        # If x greater, ignore left half
##        if (res > 0):
##            l = m + 1
##  
##        # If x is smaller, ignore right half
##        else:
##            r = m - 1
##  
##    return -1
##
#### Driver Code

##  
##    if (result == -1):
##        print("Element not present")
####    else:
##        print(simpan.baca[result-1].nama)

##TUGAS2
##kumpulan = simpan.baca
##def binarySearch(kumpulan, target):
##   # Mulai dari seluruh runtutan elemen
##   low = 0
##   high = len(kumpulan) - 1
## 
##   # Secara berulang belah runtutan itu menjadi separuhnya sampai targetnya ditemukan
##   while low <= high:
##      mid = (high + low) // 2  # Temukan pertengahan runtut itu
####      midp = L[mi]
##      if str(kumpulan[mid]) == str(target):  # Apakah pertengahannya memuat target?
##         return True
##      if str(target) < str(kumpulan[mid]): # Ataukah targetnya di sebelah kirinya?
##         high = mid - 1
##      else: # Ataukah targetnya di sebelah kanannya?
##         low = mid + 1
##   return False # Jika runtutnya tidak bisa dibelah lagi, berarti targetnya tidak ada
##
##class cari():
##    def __init__(self,parameter):
##        self.jj = parameter.split('\n')
##        self.baca = []
##        for i in range(0,10):
##            self.baca.append(Koran(self.jj[i]))
##    def binarySearch(kumpulan, target):
##    # Mulai dari seluruh runtutan elemen
##        low = 0
##        high = len(kumpulan) - 1
## 
##   # Secara berulang belah runtutan itu menjadi separuhnya sampai targetnya ditemukan
##while low <= high:
##      mid = (high + low) // 2  # Temukan pertengahan runtut itu
##      if kumpulan[mid] == target:  # Apakah pertengahannya memuat target?
##         cari = kumpulan [mid-2]
##         return cari
##      elif target < kumpulan[mid]: # Ataukah targetnya di sebelah kirinya?
##         high = mid - 1
##      else: # Ataukah targetnya di sebelah kanannya?
##         low = mid + 1
##   return False 
