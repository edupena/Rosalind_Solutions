def counter(chain,seq):
	count = 0
	for i in range(0,len(chain)-len(seq)+1):
		if chain[i:i+len(seq)]==seq:
			count +=1
	return count

LETTERS = ['A','C','G','T']
f=open("data")
lines = f.readlines()
f.close()

chain = ''.join(lines[1:]).replace("\n","")

# Compose 4-mers
A=[]
for a in LETTERS:
	for b in LETTERS:
		for c in LETTERS:
			for d in LETTERS:
				kmer = ''.join([a,b,c,d])
				A.append(counter(chain,kmer))
				
for i in A:
	print i,
