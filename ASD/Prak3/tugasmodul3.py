####NO 1
##print('Nomor 1')
##
#### mengecek ukuran matriks contoh 2 x 2 ; 2 x 3 dll
##
#### inputnya matriks 
#### [[1,2],
#### [2,3]]
##
#### mengukur matriks
##
##def ukuranMetriks(data):
##    for x in data:
##        ## cek apakah berupa list
##        if type(x) is list:
##            ## cek apakah matriks konsisten kolomnya
##            if len(x) != len(data[0]):
##                return "Matriks tidak konsisten"
##                break
##            ## cek apakah matrik hanya 2d atau lebih
##            for i in x:
##                if type(i) is list:
##                    return "Matriks tidak konsisten" 
##                    break
##        else:
##            return "Matriks tidak konsisten" 
##            break   
##    # mengembalikan baris x kolom matriks berupas list [baris,kolom]
##    return [len(data),len(data[0])]
##
###matrik A contoh benar
##A = [[1,2],[2,3],[3,3]]
##print(ukuranMetriks(A))
##
###matrik A contoh salah kolom tidak konsisten
##A = [[1,2],[2,3],[3,3,4]]
##print(ukuranMetriks(A))
##
###matrik A contoh salah isi list di dalam list
##A = [[1,2],[2,3],[3,[3,4]]]
##print(ukuranMetriks(A))
##
###matrik A contoh salah isi berupa integer bukan list
##A = [1,2,[2,3],[3,[3,4]]]
##print(ukuranMetriks(A))
##
##print()
##print()
#### untuk menjumlahkan 2 matrix
##def jumlahkan(a,b):
##    #cek apakah ke 2 matriks sama ukuranya
##    if ukuranMetriks(a) == ukuranMetriks(b) and ukuranMetriks(a) != "Matriks tidak konsisten" and ukuranMetriks(a) != "Matriks tidak konsisten":
##        #menghitung matriksnya
##        hasil=[]
##        for x in range(len(a)):
##            #print(x)
##            newbaris=[]
##            for j in range(len(a[x])):
##                # cek sequence
##                print(a[x][j],b[x][j])
##                print(a[x][j]+b[x][j])
##                newbaris.append(a[x][j]+b[x][j])
##            print("####")
##            print(newbaris)
##            hasil.append(newbaris)
##        
##        # prin lebih rapi seperti matriks
##        strhasil="Hasil penjumlahan matriks :\n"
##        for p in hasil:
##            strhasil+=str(p)+'\n'
##        strhasil+="\n hasil dalam list : "+str(hasil)
##        return strhasil
##
##
##     
##
##    elif ukuranMetriks(a) == "Matriks tidak konsisten" or ukuranMetriks(a) == "Matriks tidak konsisten":
##        return "cek lagi tipe data atau penulisan matriks kamu"
##    else:
##        return "cek lagi tipe data atau penulisan matriks kamu"
##    
##
####test penjumlahan
##b = [
##    [5,0],
##    [2,6]
##    ]
##
##c = [
##    [1,0],
##    [4,2]
##    ]
##print(jumlahkan(b,c))
##
#### pekalian matrix
#### untuk menjumlahkan 2 matrix
##def kalikan(a,b):
##    #cek apakah ke 2 matriks sama ukuranya
##    if ukuranMetriks(a) == ukuranMetriks(b) and ukuranMetriks(a) != "Matriks tidak konsisten" and ukuranMetriks(a) != "Matriks tidak konsisten":
##        #menghitung matriksnya
##        hasil = []
##        for x in range(0, len(a)):
##            newbaris = []
##            for y in range(0, len(a[0])):
##                total = 0
##                for z in range(0, len(a)):
##                    total = total + (a[x][z] * b[z][y])
##                newbaris.append(total)
##            hasil.append(newbaris)
##        
##        # prin lebih rapi seperti matriks
##        strhasil="Hasil perkalian matriks :\n"
##        for p in hasil:
##            strhasil+=str(p)+'\n'
##        strhasil+="\n hasil dalam list : "+str(hasil)
##        return strhasil
##
##
##     
##
##    elif ukuranMetriks(a) == "Matriks tidak konsisten" or ukuranMetriks(a) == "Matriks tidak konsisten":
##        return "cek lagi tipe data atau penulisan matriks kamu"
##    else:
##        return "cek lagi tipe data atau penulisan matriks kamu"
##
##print(kalikan(b,c))
##
##
###mencari determinan
##def determinant(matrix, mul):
##
##    width = len(matrix)
##    if width == 1:
##        return mul * matrix[0][0]
##    else:
##        sign = -1
##        answer = 0
##        for i in range(width):
##            m = []
##            for j in range(1, width):
##                buff = []
##                for k in range(width):
##                    if k != i:
##                        buff.append(matrix[j][k])
##                m.append(buff)
##            sign *= -1
##            answer = answer + mul * determinant(m, sign * matrix[0][i])
##    return answer
##A = [[-2,2,-3],[-1,1,3],[2,0,-1]]
##Det = determinant(A,1)
##print(Det)
##
##print()
##print()
##
####NO 2
##print('Nomor 2')
##
##def buatNol(m,n=0):
##    if n==0:
##        # buat matrix bujur sangkat
##        return [ [0 for j in range(m)] for i in range(m) ]
##    else:
##        return [ [0 for j in range(m)] for i in range(n) ]
##
##def buatIdentitas(m):
##    return [[1 if j==i else 0 for j in range(3)] for i in range(3)]
##
##print(buatNol(4))
##print(buatNol(4,2))
##print(buatIdentitas(4))
##
##
##print()
##print()
##
####NO 3
##print('Nomor 3')
##
##class Node(object):
##    """
##    membuat node
##    """
##    def __init__(self,data,next=None):
##        self.data = data
##        self.next = next
##
###buat linkedin list dengan head 'linke'
##a = Node(35)
##b = Node(40)
##c = Node(33)
##d = Node(13)
##e = Node(43)
##
##linke = a
##linke.next = b
##b.next = c
##c.next = d
##d.next = e
##
##print(linke.next.data)
##
#### cetak linkedlist
##def cetak(head):
##    headnya = head
##    while headnya is not None:
##        print(headnya.data)
##        headnya = headnya.next
##        
##
#### cari(head,yangdicari)
##def cari(head,yangdicari):
##    headnya = head
##    node = 1
##    while headnya is not None:
##        if headnya.data == yangdicari:
##            return str(headnya.data) + " Pada Node Ke : "+str(node)
##            break
##        else:
##            headnya = headnya.next
##            node+=1
##        
##    
##print()
##print(cari(linke,13))
##
#### tambahDepan(head)
##def tambahDepan(head):
##    """Menambah node pada awal/depan list dengan membuat node baru lalu menyimpan linked list sebelumnya yang berada di head ke temp variabel
##        setelah itu linked list yang bead di temp variabel dimasukan kedalam head baru yang berasal dari node baru"""
##    nodelama = head
##    nodebaru = Node(0)
##    nodebaru.next = nodelama
##    return nodebaru
##
##linkeDepan = tambahDepan(linke)
##cetak(linkeDepan)
#### tambahAkhir(head)
##def tambahAkhir(head,isi=0):
##    """Menambah node di akhir list dengan membuat node baru ke next pointer dari node paling terakhir list sekarang"""
##    #iterasi jika none maka tambahkan satu data baru tersewbut lalu break
##    headnya = head
##    while headnya is not None:
##        print(headnya.data)
##        if headnya.next is None:
##            if isi == 0:
##                headnya.next = Node(0)
##            else:
##                headnya.next = Node(isi)
##            return headnya
##            break
##        headnya = headnya.next
##
##print()
##cetak(tambahAkhir(linkeDepan))
#### tambah(head,posisi) menyisipkan node setelah posisi node yang disebutkan
##def tambah(head,posisi):
##    headnya = head
##    jml = 1
##    while headnya is not None:
##        print(headnya.data)
##        if posisi-1 == jml:
##            headnya = headnya.next.next
##            jml+=1
##        else:
##            headnya = headnya.next
##            jml+=1
##
##print("SISIPKAN")
##cetak(linke)
##print()
##cetak(tambah(linke,3))
##
#### hapus(posisi)
##print("MENGHAPUS")
##def hapus(head, posisi):
##        prev = None
##        curr = head
##        while curr:
##            if curr == posisi:
##                if prev:
##                    prev.setNextNode(curr.getNextNode())
##                else:
##                    self.head = curr.getNextNode()
##                return True
##                    
##            prev = curr
##            curr = curr
##            
##        return False
##cetak(linke)
##
##print("HAPUS LIST")
##print()
##hapus(linke,3)
##
##
##
##print()
##print()
##
##
