import itertools

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

def spacesOnlyAtEnd(p):
	p=p[::-1]
	letter=False
	for i in p:
		if i==" " and letter:
			return False
                if i!=" ":
                        letter=True

	return True

f=open("data")
lines = f.readlines()
f.close()

LETTERS = lines[0].replace("\n","").split(" ")
size = int(lines[1].replace("\n",""))

for w in range(size-1):
	LETTERS.insert(0," ")


perms = list(itertools.product(''.join(LETTERS),repeat=size))
perms = f7(perms)
for elem in perms[1:]:
	if spacesOnlyAtEnd(elem):
	        print ''.join(elem)


