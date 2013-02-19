def overlap(s1,s2,l):
	for w in range(l,min(len(s1),len(s2))+1):
		if (s1[-w:]==s2[:w]):
			return w
	return False

def glue(s1,s2,l):
	return s1[:-l]+s2



f=open("data")
lines = f.readlines()

l = len(lines[0].replace("\n",""))/2+1

repeat = True

total = lines[0].replace("\n","")
while repeat:
	repeat=False
	for n in range(1,len(lines)):
		lines[n] = lines[n].replace("\n","")
		ov_left = overlap(lines[n],total,l)
		ov_right = overlap(total,lines[n],l)
		if ov_left:
			total=glue(lines[n],total,ov_left)
			lines[n]=""
			repeat = True
		elif ov_right:
			total=glue(total,lines[n],ov_right)
			lines[n]=""
                        repeat = True
print total

