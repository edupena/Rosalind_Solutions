import itertools

f=open("data")
lines = f.readlines()
f.close()

LETTERS = lines[0].replace("\n","").split(" ")
size = int(lines[1].replace("\n",""))

perms = list(itertools.product(''.join(LETTERS),repeat=size))
for elem in perms:
	print ''.join(elem)
	

