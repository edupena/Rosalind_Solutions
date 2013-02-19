f=open("rosalind_dna.txt")

line = f.readline()

print line.count("A"),
print line.count("C"),
print line.count("G"),
print line.count("T")


print f.readline()
