k=3

f=open("data")
lines =  f.readlines()


chains = ''.join(lines).replace("\n>",">").replace("A\n","A").replace("C\n","C").replace("T\n","T").replace("G\n","G").split(">")[1:]

for chain in chains:
	[cid,cchain] = chain.split("\n")
	for itchain in chains:		
		[itcid,itcchain] = itchain.split("\n")
		if itcid!=cid:
			if cchain[-k:]==itcchain[:k]:
				print cid,itcid

f.close()

