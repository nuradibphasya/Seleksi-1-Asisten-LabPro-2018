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
if(ada==0): #Kalau tidak ada kunci yang harus diduplikat, maka akan menghasilkan keluaran string "Tidak ada" menandakan bahwa tida ada kunci yang perlu diduplikat
	print ("Tidak ada")