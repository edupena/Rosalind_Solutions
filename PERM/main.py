import itertools



f=open("data")
value = int(f.readline().replace("\n",""))
f.close()

perm = list(itertools.permutations(range(1,value+1)))

print len(perm)
for p in perm:
	for c in p:
		print c,
	print
