##Latihan pertama
def cariLurus(wadah, target):
    n = len(wadah)
    for i in range(n):
        if wadah[i] == target:
            return True
    return False

##Latihan kedua
class MhsTIF(object):
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangSaku = vars
    def __str__(self):
        s = self.nama + ', nim ' + str(self.nim)\
        + '. Tinggal di ' + self.kota\
        + '. Uang saku Rp ' + str(self.uangSaku)\
        + '. tiap bulannya.'
        return s
##Daftar = [MhsTIF('Ika',10,'Sukoharjo',240000),
##MhsTIF('Budi',51,'Sragen',230000),
##MhsTIF('Ahmad',2,'Surakarta',250000),
##MhsTIF('Chandra',18,'Surakarta',235000),
##MhsTIF('Eka',4,'Boyolali',240000),
##MhsTIF('Fandi',31,'Salatiga',250000),
##MhsTIF('Deni',13,'Klaten',245000),
##MhsTIF('Galuh',5,'Wonogiri',245000),
##MhsTIF('Janto',23,'Klaten',245000),MhsTIF('Hasan',64,'Karanganyar',270000),
##MhsTIF('Khalid',29,'Purwodadi',265000)]
##
##target = 'Klaten'
##for i in Daftar:
##    if i.kota == target:
##        print (i.nama + ' tinggal di ' + target)

