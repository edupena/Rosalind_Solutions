f=open("data")
print f.readline().replace("A","W").replace("C","V").replace("T","A").replace("G","C").replace("W","T").replace("V","G")[::-1]

f.close()
