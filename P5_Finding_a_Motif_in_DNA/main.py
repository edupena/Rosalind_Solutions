f=open("data")
chain = f.readline().replace("\n","")
subchain = f.readline().replace("\n","")
f.close()
pos=0
for p in range(len(chain)-len(subchain)+1):
	if chain[p:p+len(subchain)]==subchain:
		print p+1,
