f=open("data")
lines = f.readlines()
f.close()


lines[0]=lines[0].replace("\n","")
lines[1]=lines[1].replace("\n","")

dist = 0
for i in range(len(lines[0])):
	if (lines[0][i]!=lines[1][i]):
		dist+=1

print dist
	
