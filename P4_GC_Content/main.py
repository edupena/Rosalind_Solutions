f=open("data")
lines =  f.readlines()# [0].split(">")


chains = ''.join(lines).replace("\n>",">").replace("A\n","A").replace("C\n","C").replace("T\n","T").replace("G\n","G").split(">")[1:]

chain = chains[0]
[id_longest,chain_longest] = chain.split("\n")
GC = chain_longest.count("C")+chain_longest.count("G")
total = len(chain_longest)
count_longest = 100*float(GC)/total

for chain in chains[1:]:
	[cid,cchain] = chain.split("\n")
	GC = cchain.count("C")+cchain.count("G")
	total = len(cchain)
	count = 100*float(GC)/total
	if (count>count_longest):
		id_longest = cid
		count_longest = count

print id_longest
print str(count_longest)+"%"

f.close()
