## Latihan 1.1
print("Latihan 1.1")
a = 4
b = 5
c = a+b
print("nilai a",a)
print("nilai b", b)
print("sekarang, c = a+b =", a, "+", b, "=", c)
print('')
print('sudah selesai')

## Latihan 1.2
print("======================================================")
print("")
print("Latihan 1.2")
print('kita perlu bicara sebentar')
nm = input('Siapa namamu? (ketik disini) > ')
print ('selamat belajar ', nm)
angkaStr=input('Masukkan sebuah angka antara 1 sampai 100 =')
a = int(angkaStr)
kuadrat = a*a
print(nm, 'tahukah kamu bahwa', a, 'kuadrat adalah', kuadrat, '?')

##latihan 1.3
print("======================================================")
print("")
print("Latihan 1.3")
def ucapkanSalam():
    print("assalamualaikum")
def sapa(nama):
    ucapkanSalam()
    print("halo", nama)
    print("selamat belajar")
def kuadratkan(b):
    h = b*b
    return h
ucapkanSalam()
sapa('Edy Susilo')
b = kuadratkan(5)
b
k = 9
print("Bilangannya",k, ", kalau dipangkatkan dua jadinya", kuadratkan(k))

## Latihan 1.4
print("======================================================")
print("")
print("Latihan 1.4")
from math import sqrt as akar
def selesaikanABC(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    d = b**2 - 4*a*c
    x1 = (-b + akar(d))/(2*a)
    x2 = (-b - akar(d))/(2*a)
    hasil = (x1, x2)
    return hasil
k = selesaikanABC(1, -5,6)
print(k)
print(k[0])
print(k[1])

## Latihan 1.5
print("======================================================")
print("")
print("Latihan 1.5")
def apakahGenap(x):
    if (x%2 == 0):
        return True
    else:
        return False
a = 46
b = 17
print("bilangan genap",a,apakahGenap(a))
print("bilangan genap",b,apakahGenap(b))

## Latihan 1.6
print("======================================================")
print("")
print("Latihan 1.6")
def tigaAtauLima(x):
    if (x%3==0 and x%5==0):
        print('Bilangan', x ,'adalah kelipatan 3 dan 5 sekaligus')
    elif x%3==0:
        print('Bilangan', x ,'adalah kelipatan 3')
    elif x%5==0:
        print('Bilangan', x ,'adalah kelipatan 5')
    else:
        print('Bilangan', x ,'bukan kelipatan 3 atau 5')
tigaAtauLima(9)
tigaAtauLima(10)
tigaAtauLima(15)
tigaAtauLima(17)


## Latihan 1.7
print("======================================================")
print("")
print("Latihan 1.7")
staff = { 'Santi' : 'santi@ums.ac.id', \
          'Jokowi' : 'jokowi@solokab.go.id', \
          'Endang' : 'endang@yahoo.com', \
          'Sulastri' : 'sulastri@gmail.com' }
yangDicari = 'Santi'
if yangDicari in staff:
    print('Emailnya', yangDicari, 'adalah', staff[yangDicari])
else:
    print('Tidak ada yang namanya', yangDicari)

          
## Latihan 1.8
print("======================================================")
print("")
print("Latihan 1.8")
for i in range(0,10):
    print(i)

## Latihan 1.9
print("======================================================")
print("")
print("Latihan 1.9")
s = "Ini Budi"
for i in s:
    print(i)

## Latihan 1.10
print("======================================================")
print("")
print("Latihan 1.10")
dd={'nama':'joko','umur':21,'asal':'surakarta'}
for kunci in dd:
    print(kunci, '<------>', dd[kunci])

## Latihan 1.11
print("======================================================")
print("")
print("Latihan 1.11")
bil = 0
while(bil*bil<200):
    print(bil, bil*bil)
    bil = bil+1
    













