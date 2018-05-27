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

