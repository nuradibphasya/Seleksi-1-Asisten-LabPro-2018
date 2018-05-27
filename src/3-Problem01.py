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
