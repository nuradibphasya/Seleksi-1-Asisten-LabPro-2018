NIM  : 18216012
Nama : Aulia Nur Adib Phasya


- Bab 1 Problem 03

Deskripsi : 
Diberikan masukan berupa besar nilai sudut s (masukan diasumsikan selalu berada pada rentang nilai 0-360), program akan mengeluarkan output berupa sin(a)=sin(b) atau sin(a) = -sin(b), dimana a merupakan nilai masukan berupa s dan b merupakan nilai dalam rentang 0-90 dan keluaran tergantung besar nilai masukan s

Source Code : 

sudut =  int(input("Masukan besar sudut: ")) #Asumsi input selalu berada pada rentang 0-360
	
if sudut>=0 and sudut<=90:
	print ("sin(%d) = sin(%d)" % (sudut,sudut))
elif sudut>90 and sudut<=180:
	print ("sin(%d) = sin(%d)" % (sudut,180-sudut))
elif sudut>180 and sudut<=270:
	print ("sin(%d) = -sin(%d)" % (sudut,sudut-180))
else:
	print ("sin(%d) = -sin(%d)" % (sudut,360-sudut)) 

Penjelasan :
Awalnya program meminta masukan berupa sebuah nilai yang menyatakan besar sudut yang disimpan dalam variabel sudut. Program akan mengeluarkan output tergantung besar nilai masukannya. Jika rentang nilai masukan 0-90, output dari program tersebut adalah "sin(sudut) = sin(sudut)". Jika rentang nilai masukan 91-180, outputnya adalah "sin(sudut) = sin(180-sudut)". Jika rentang nilai masukan 181-270, outputnya adalah "sin(sudut) = -sin(sudut-180)" dan jika rentang nilai masukannya 271-360, outputnya adalah "sin(sudut) = -sin(360-sudut)"


- Bab 2 Problem 02

Deskripsi : 
Diberikan masukan berupa nilai x, nilai y dan tipe yang masukannya berupa "A", "B" atau "C". Keluaran berupa bilangan-bilangan yang sesuai dengan tipe bilangan yang dimasukan. Apabila tidak ada bilangan yang memenuhi, maka program akan menghasilkan keluaran string "Tidak ada"

Source Code : 

x = int(input("Masukan X :"))
y = int(input("Masukan Y :"))
tipe = str(input("Masukan tipe bilangan :")) #Asumsi masukan tipe selalu A, B atau C
print ("Tipe bilangan %s pada rentang %d sampai %d adalah" % (tipe,x,y))
ada = 0

if (tipe == "A"):
	for n in range (x,y+1):
		total = 0
		bil = 1
		while ( bil < n ) :
			if (n % bil == 0):
				total = total + bil
			bil+=1
		if (n > total):
			ada+=1
			print (n)
	if (ada==0):
		print ("Tidak ada")
elif(tipe == "B"):
	for n in range (x,y+1):
		total = 0
		bil = 1
		while ( bil < n ) :
			if (n % bil == 0):
				total = total + bil
			bil+=1
		if (n == total):
			ada+=1
			print (n)	
	if (ada==0):
		print ("Tidak ada")
elif(tipe == "C"):
	for n in range (x,y+1):
		total = 0
		bil = 1
		while ( bil < n ) :
			if (n % bil == 0):
				total = total + bil
			bil+=1
		if (n < total):
			ada+=1
			print (n)
	if (ada==0):
		print ("Tidak ada")

Penjelasan :
Awalnya program meminta masukan berupa x dan y, dimana x dan y merupakan range dari bilangan-bilangan yang akan dicari apakah memenuhi suatu tipe bilangan tertentu atau tidak. Kemudian program juga meminta masukan berupa tipe bilangan (input A,B atau C) yang nilainya disimpan dalam variabel tipe.

Kemudian lakukan looping dalam range x sampai y. Variabel n merupakan berisi nilai bilangan yang memiliki rentang x-y yang akan dicek apabila memenuhi kriteria tipe bilangan tertentu atau tidak dengan mengecek jumlah seluruh faktor dari n yang disimpan ke dalam variabel total. Variabel total merupakan jumlah dari semua bilangan yang habis membagi n, dalam soal ini n tidak termasuk faktor bilangan. Kemudian lakukan pengecekan variabel total dengan n sesuai dengan tipe bilangan yang dimasukkan. Jika tipe bilangannya A, keluaran berupa bilangan-bilangan yang jumlah semua faktornya lebih kecil daripada bilangan tersebut. Jika tipe bilangannya B, keluaran berupa bilangan-bilangan yang jumlah semua faktornya sama dengan bilangan tersebut dan jika tipe bilangannya C, keluaran berupa bilangan yang jumlahnya lebih besar dari bilangan tersebut. Jika tidak ada bilangan yang sesuai dengan tipe bilangan tersebut, maka program mengeluarkan output string "Tidak ada"


- Bab 3 Problem 01

Deskripsi : 
Diberikan sebuah input masukan berupa suatu nilai n. Jika ada nilai x (Rentang 1-29) yang memenuhi fungsi f(x), program akan mengeluarkan output berupa nilai x yang menghasilkan nilai n tersebut dan jika tidak ada yang memenuhi, program akan mengeluarkan output string "Tidak ada x yang sesuai"

Source Code : 

def kalkulus(x):
	i=1
	bil=-1
	while (i<30 and bil<0):
		hasil = 2*(i**5) + 3*(i**4) + 9*(i**3) - (i**2) + 3*i - 2 
		if hasil==x:
			bil=i
		i+=1
	if(bil!=-1):
		print ("Nilai x adalah %d" % (bil))
	else:
		print ("Tidak ada x yang sesuai")


nilai = int(input ("Masukan f(x) : "))
kalkulus(nilai)

Penjelasan : 
Program akan meminta sebuah masukan berupa sebuah nilai yang disimpan dalam variabel nilai. Kemudian nilai tersebut akan dimasukkan ke dalam fungsi kalkulus(nilai) dengan parameter berupa variabel nilai. Fungsi kalkulus akan mengecek apakah ada bilangan dari 1-29 yang memenuhi f(x)=2x^5 + 3x^4 + 9x^3 - x^2 + 3x - 2 sehingga nilai f(x) tersebut sama besar dengan nilai pada variabel nilai. Jika ada variabel yang sama, maka program akan mengeluarkan output berupa nilai x yang memenuhi f(x) tersebut. Jika tidak, program akan mengeluarkan output string "Tidak ada x yang sesuai"


- Bab 4 Problem 12

Deskripsi : 
Diberikan sebuah masukan berupa n yaitu jumlah kunci dengan n masukan berikutnya berupa n nomor ruangan kunci tersebut. Program menghasilkan keluaran berupa nomor-nomor kunci yang harus diduplikat. Jika tidak ada kunci yang harus diduplikat, maka program akan mengeluarkan string "Tidak ada"

Source Code : 

kunci = int(input("Masukkan jumlah kunci yang ada : "))
print ("Masukkan nomor ruangan kunci yang ada :")

ruang=[]
for i in range (kunci):
	nomor=input()
	ruang.append(nomor)

ada=0
print ("Kunci yang harus diduplikat :")
for i in range (kunci):
	totalkunci=ruang.count(ruang[i])
	if(totalkunci==1):
		print (ruang[i])
		ada+=1
if(ada==0): #Kalau tidak ada kunci yang harus diduplikat, maka akan menghasilkan keluaran string "Tidak ada" menandakan bahwa tidak ada kunci yang perlu diduplikat
	print ("Tidak ada")

Penjelasan : 
Program akan meminta masukan berupa n, yaitu jumlah kunci yang ada. Kemudian meminta masukan berikutnya sebanyak n buah, yaitu ruangan dari kunci-kunci yang tersedia. Nilai-nilai tersebut dimasukkan ke dalam array ruang. Variabel ada menghitung jumlah kunci yang frekuensi kemunculannya hanya sekali. Lalu lakukan looping untuk i dari range 0 sampai n-1. Variabel totalkunci menyimpan nilai jumlah kemunculan kunci (ruang[i]) pada array ruang. Jika jumlah kemunculannya sama dengan 1, nilai ada akan bertambah sebesar 1 dan mengeluarkan output berupa nilai ruang[i] tersebut. Jika pada akhir loop variabel ada tetap bernilai 0, maka program akan mengeluarkan output string "Tidak ada"

Pada awalnya 

- Bab 5 Problem 11

Deskripsi : Program membaca file eksternal berupa queue.txt, keluaran yang dihasilkan dari program tersebut adalah string "file loaded!" menandakan file berhasil dibaca dan sebuah bilangan yang merepresentasikan antrian terpanjang dari matriks yang dibaca dari queue.txt tersebut. 

Source Code : 

antri = open('queue.txt','r')

w,h = [int(x) for x in next(antri).split()]
matrix = [[int(x) for x in line.split()] for line in antri]
print ("file loaded!")

maks=-1

for i in range (len(matrix)):
	pjg=0
	for j in range(len(matrix[i])):
		if(matrix[i][j]==1):
			pjg+=1
	if(maks<pjg):
		maks=pjg

print (maks)
antri.close()

Penjelasan :
Program membaca masukan berupa file eksternal queue.txt yang isinya berupa matriks berukuran n kali m dan isinya. Matriks hanya bernilai 0 dan 1. 0 menandakan slot kosong dan 1 menandakan slot sudah terisi oleh orang. Variabel maks menyimpan nilai berupa antrian terpanjang dari matriks tersebut. Lakukan looping dengan range 0 sampai n dan buat looping lagi didalamnya dengan range 0 sampai m. Untuk setiap baris, kemudian hitung jumlah kemunculan 1 pada setiap baris dari matriks tersebut. Jika nilai pjg lebih besar dari maks, nilai maks akan diinisiasi dengan nilai pjg.
Output dari program ini adalah antrian terpanjang dari matriks tersebut. 