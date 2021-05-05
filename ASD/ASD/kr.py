####NO 1
class Koran(object):
    def __init__(self,nama,kota,kodepos,url,berdiri):
        self.nama = nama
        self.kota = kota
        self.kodepos = kodepos
        self.url = url
        self.berdiri = berdiri
    def __str__(self):
        s = str(self.nama) + " - "+ str(self.url)
        return s
##NO 2
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

####NO 3
class Teks(object):
    def __init__(self, n):
        self._data = n * [None]
    def __getitem__(self, key):
        return self._data[key]
    def __setitem__(self, key, value):
        if key >= len(self._data):
            q = key - len(self._data) + 1
            li = q * [None]
            self._data.extend(li)
        self._data[key] = value
#Nomor 4 
    def simpan(self, par):
        baris = par.splitlines()
        baca = []
        for x in baris[1::]:
            hasil = x.split(";")
            baca.append(hasil)
        tambah = len(baca) - len(self._data)
        self.__setitem__(tambah,None)
        for x in range(len(self._data)):
            new = Koran(baca[x][0],baca[x][1],baca[x][2],baca[x][3],baca[x][4])
            self.__setitem__(x,new)
## Tugas 2

    def cari(self,target):
        kumpulan = self._data
        low = 0
        high = len(kumpulan)-1
        x = []
        y = -1

        if target == kumpulan[1].kodepos:
            y = 1
        elif target == kumpulan[2].kodepos:
            y = 2
        elif target == kumpulan[3].kodepos:
            y = 3
        elif target == kumpulan[4].kodepos:
            y = 4
        elif target == kumpulan[5].kodepos:
            y = 5
        elif target ==kumpulan[6].kodepos:
            y = 6
        elif target == kumpulan[7].kodepos:
            y = 7
        elif target == kumpulan[8].kodepos:
            y = 8
        elif target == kumpulan[9].kodepos:
            y = 9
        elif target == kumpulan[10].kodepos:
            y = 10
        else :
            y = -1
        
        while low <= high:
            mid = (high + low) // 2
            if mid == y:
                return self._data[mid].nama
            elif y < mid:
                high = mid - 1
            else:
                low = mid + 1
        return False

## Membuat array
a = Teks(11)
## Memanggil method simpan
a.simpan(krn)

