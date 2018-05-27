sudut =  int(input("Masukan besar sudut: ")) #Asumsi input selalu berada pada rentang 0-360
	
if sudut>=0 and sudut<=90:
	print ("sin(%d) = sin(%d)" % (sudut,sudut))
elif sudut>90 and sudut<=180:
	print ("sin(%d) = sin(%d)" % (sudut,180-sudut))
elif sudut>180 and sudut<=270:
	print ("sin(%d) = -sin(%d)" % (sudut,sudut-180))
else:
	print ("sin(%d) = -sin(%d)" % (sudut,360-sudut)) 
