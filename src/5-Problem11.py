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