##Soal untuk mahasiswa
print("Soal untuk mahasiswa")
print("==========================")
print('')

## No1
print('No 1')

def cetakSiku(x):
    for i in range(0, x):
        for j in range(0, i + 1):
            print('* ' , end='')
        print('')
cetakSiku(5)

## No2
print("")
print("==========================")
print("")
print("No 2")
def gambarlahPersegiEmpat(x,y) :
    for i in range(x):
        if (i == 0 or i== x-1) :	
            print ("@ "*(y))
        else :
            print ("@  "+" "*(y-1)+" @")
gambarlahPersegiEmpat(4,5)


## No3
## a
print("")
print("==========================")
print("")
print("No 3a")
def jumlahHurufVokal(s):
    panjangkata = len(s)
    i = 0
    vokal = ['a','i','u','e','o','A','I','U','E','O']
    jumlahVokal = 0
    while i < panjangkata:
        if s[i] in vokal :
            jumlahVokal += 1
        i+=1
    print("(",panjangkata,",",jumlahVokal,")")
jumlahHurufVokal("Surakarta")

## b
print("")
print("==========================")
print("")
print("No 3b")
def jumlahHurufKonsonan(s):
    panjangkata = len(s)
    i = 0
    vokal = ['a','i','u','e','o','A','I','U','E','O']
    jumlahKonsonan = 0
    while i < panjangkata:
        if s[i] not in vokal :
            jumlahKonsonan += 1
        i+=1
    print("(",panjangkata,",",jumlahKonsonan,")")
jumlahHurufKonsonan("Surakarta")
## 4
print("")
print("==========================")
print("")
print("No 4")
def rerata(x):
    n=int(len(x))
    hasil=sum(x)/n
    return hasil
print(rerata([1,2,3,4,5]))


## 5
print("")
print("==========================")
print("")
print("No 5")
from math import sqrt as sq
def apakahPrima(n):
    n = int(n) 
    assert n >=0 
    primaKecil = [2,3,5,7,11] 
    bukanPrKecil = [0,1,4,6,8,9,10]
    if n in primaKecil:
        return True
    elif n in bukanPrKecil:
        return False
    else:
        for i in range(2,int(sq(n))+1):
            if n % i==0:
                return False
        return True   
print(apakahPrima(17))
print(apakahPrima(97))
print(apakahPrima(123))

#No 6
print("")
print("==========================")
print("")
print("No 6")
bil1 = 2 
bilend = 100
print("Bilangan prima antara",bil1,"and",bilend,":") 
for num in range(bil1,bilend + 1): 
    if num > 1: 
        for i in range(2,num): 
            if (num % i) == 0: 
                break 
        else: 
            print(num, 'Adalah Bilangan Prima dari 2 sampai 100') 

#NO 7
print("")
print("==========================")
print("")
print("No 7")
# fungsi untuk mencari faktorisasi prima sebuah bilangan
def faktorPrima(n):
    factor=[]
    loop=2
    while loop <= n:
        if n % loop ==0:
            n /= loop
            factor.append(loop)
        else:
            loop+=1
    return factor
print(faktorPrima(10))
print(faktorPrima(120))

## 8
print("")
print("==========================")
print("")
print("No 8")
from re import search
def apakahTerkandung(a,b):
    if search(a,b):
        print("true")
    else:
        print("False")
h = 'do'
k = 'Indonesia tanah air beta'
apakahTerkandung(h,k)
apakahTerkandung('pusaka',k)

#NO 9
print("")
print("==========================")
print("")
print("No 9")
for i in range(1,50):
   if i%3==0 and i%5==0:
       i='Pyton UMS'
   elif i%5 ==0:
       i='UMS'
   elif i%3==0:
       i='Python'
   print(i)

##10
print("")
print("==========================")
print("")
print("No 10")
def selesaikanABC(a,b,c):
    det = b**2 - 4*a*c
    if det < 0 :
        print("Determinannya negatif. Persamaan tidak mempunyai akar real.")
    else:
        print("Determinannya = " , det)
selesaikanABC(1,2,3)
## 11
print("")
print("==========================")
print("")
print("No 11")
def apakahKabisat(a):
    if a % 100 == 0:
        if a % 400 == 0:
            print(a, "tahun kabisat")
        else:
            print(a,"bukan tahun kabisat")
    elif a%4 == 0:
        print(a, "tahun kabisat")
    elif a%4 != 0:
        print(a,"bukan tahun kabisat")
apakahKabisat(1806)
apakahKabisat(1900)
apakahKabisat(2000)
apakahKabisat(2001)
apakahKabisat(2014)

## 12
print("")
print("==========================")
print("")
print("No 12")
from random import randint
b = randint(1,100)
print('Permainan Tebak Angka')
print('Saya Menyimpan sebuah angka bulat antara 1 sampai 100')
n = -1
m = 0
while n != b :
    m +=1
    print("masukkan tebkan ke-", m, "> ", end = (''))
    n = int(input())
    if n == b:
        print('Ya, Anda Benar')
    elif n > b:
        print('Terlalu Besar, Coba lagi')
    else:
        print('Terlalu Kecil, Coba lagi')

## 13
print("")
print("==========================")
print("")
print("No 13")
def Terbilang(bil):
    angka = ["","Satu","Dua","Tiga","Empat","Lima","Enam",
             "Tujuh","Delapan","Sembilan","Sepuluh","Sebelas"]
    Hasil = " "
    n = int(bil)
    if n>= 0 and n <= 11:
        Hasil = angka[n]
    elif n <20:
        Hasil = Terbilang (n-10) + " Belas "
    elif n <100:
        Hasil = Terbilang (n/10) + " Puluh " + Terbilang (n%10)
    elif n <200:
        Hasil = " Seratus " + Terbilang (n-100)
    elif n <1000:
        Hasil = Terbilang (n/100) + " Ratus " + Terbilang (n%100)
    elif n <2000:
        Hasil = " Seribu " + Terbilang (n-1000)
    elif n <1000000:
        Hasil = Terbilang (n/1000) + " Ribu " + Terbilang (n%1000)
    elif n <1000000000:
        Hasil = Terbilang (n/1000000) + " Juta " + Terbilang (n%1000000)
    elif n <1000000000000:
        Hasil = Terbilang (n/1000000000) + " Milyar " + Terbilang (n%1000000000)
    elif n <1000000000000000:
        Hasil = Terbilang (n/1000000000000) + " Triliyun " + Terbilang (n%1000000000000)
    elif n == 1000000000000000:
        Hasil = "Satu Kuadriliun"
    else:
        Hasil = "Angka Hanya Sampai Satu Kuadriliun"

    return Hasil

print(Terbilang(123456))

##
## 14
print("")
print("==========================")
print("")
print("No 14")
def formatrupiah(uang):
    y = str(uang)
    if len(y) <= 3 :
        return ('Rp ' + y)     
    else :
        p = y[-3:]
        q = y[:-3]
        return (formatrupiah(q) + '.' + p)
        print ('Rp ' +  formatrupiah(q) + '.' + p)

print(formatrupiah(15000))
print(formatrupiah(34000))










    
            
