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
